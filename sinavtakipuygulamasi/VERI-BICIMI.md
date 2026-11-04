# veri.json biçimi (Sınav Takip Uygulaması)

Bu belge uygulamanın (`index.html`) okuduğu ve yazdığı **`veri.json`** dosyasının tam biçimidir. Aynı belge “Uygulama
Oluştur” ile açılan her dönem klasörüne kopyalanır. Kökteki `VERI-BICIMI.md` eski (v2) sürümün belgesidir; bu belge
onu temel alır ve 2. aşamada eklenen alanları (`teacherList`, `rooms`, `departments[].classes`, `settings`,
`proctorAvailability[].email`) ile 3. aşamadaki Excel sayfa/sütun eşlemesini de anlatır. Yapay zekâ oturumları için ayrıca `YZ-REHBERI.md`'ye bakın.

- Dosya UTF-8'dir; Türkçe harfler olduğu gibi yazılır. Python: `json.dumps(veri, ensure_ascii=False, indent=1) + "\n"`.
  Sitedeki düzenlemeler de dosyayı aynı biçimde (girinti 1, sonda satır sonu) geri yazar; GitHub farkında yalnız değişen satırlar görünür.
- **Sınav kayıtlarındaki** sayılar (öğrenci, kapasite) **metin** olarak yazılır: `"21"`, bilinmiyorsa `""`.
  `meta` sayımları ile 2. aşamada eklenen `rooms` ve `settings` alanlarındaki sayılar **gerçek sayıdır** (`40`, bilinmiyorsa `null`).
- Yeni alanların hepsi isteğe bağlıdır. Yoksa uygulama eski davranışla çalışır (öğretim elemanı ve derslik listeleri
  sınavlardan türetilir, ayarlar varsayılan değerleri alır). Böylece eski dönemlerin verisi (ör. `2627vizeprogrami/veri.json`) değiştirilmeden okunur.

## Genel yapı

```json
{
 "meta": { ... },
 "departments": [ ... ],
 "exams": [ ... ],
 "assignments": [ ... ],
 "teachers": [ ... ],
 "proctors": [ ... ],
 "updates": [ ... ],
 "proctorAvailability": [ ... ],
 "teacherList": [ ... ],
 "rooms": [ ... ],
 "settings": { ... },
 "envelopes": { ... }
}
```

| Alan | Zorunlu mu | Ne işe yarar |
|---|---|---|
| `meta` | Zorunlu | Kurum, dönem, demo işareti ve sayımlar. |
| `departments` | Zorunlu | Bölümler ve (isteğe bağlı) sınıfları. |
| `exams` | Zorunlu | Asıl veri: her sınav bir kayıt. |
| `assignments` | Zorunlu (türetilir) | Gözetmen görevleri; `exams`'ten hesaplanır. |
| `teachers` | Zorunlu (türetilir) | Öğretim Üyeleri sekmesindeki adlar: sınavlardaki `teacher` değerleri + `teacherList` adları. |
| `proctors` | Zorunlu (türetilir) | Gözetmenler sekmesindeki adlar: `assignments` + `proctorAvailability` adları. |
| `updates` | İsteğe bağlı | Ana Sayfa'daki “Son değişiklikler”. |
| `proctorAvailability` | İsteğe bağlı | Gözetmen kayıtları: ad, izinli gün/saatler, e-posta. |
| `teacherList` | İsteğe bağlı (2. aşama) | Öğretim elemanı kayıtları: unvan, bölüm, e-posta, izinli gün/saatler. |
| `rooms` | İsteğe bağlı (2. aşama) | Derslik kayıtları: kat, sınav kapasitesi, tam kapasite. |
| `settings` | İsteğe bağlı (2. aşama) | Uyarıların ve görev sayımının sayıları. |
| `envelopes` | İsteğe bağlı | Sınav zarfı takibi (Sınav Zarfları uygulaması). |

“Türetilir” denen alanlar elle yazılmaz (yazılırsa da site her kayıtta yeniden hesaplar); kural aşağıda.

## `meta`

| Alan | Örnek | Açıklama |
|---|---|---|
| `mode` | `"demo"` | Yalnız demo klasöründe (`sinavtakipuygulamasi/`). Varsa herkes düzenler, kayıtlar tarayıcıda kalır. Gerçek dönemde **yazılmaz**. |
| `university` | `"Örnek Üniversitesi"` | Üniversite adı (eski veride `institution`). |
| `faculty` | `"Örnek Fakültesi"` | Fakülte adı. |
| `programName` | `"2026-2027 Güz Dönemi Final"` | Dönem adı (başlıkta). |
| `period` | `"4–15 Ocak 2027"` | Sınav tarihleri (uzun tire `–`). |
| `examCount` | `120` | Sınav sayısı (başka birim gözetmenlikleri hariç). Türetilir. |
| `assignmentCount`, `teacherCount`, `proctorCount` | `90`, `45`, `14` | `assignments`, `teachers`, `proctors` uzunlukları. Türetilir. |

## `departments`

```json
{"code": "YBS", "name": "Yönetim Bilişim Sistemleri", "language": "Türkçe", "classes": ["1", "2", "3", "4"]}
```

| Alan | Kural |
|---|---|
| `code` | Kısa kod; boşluk, virgül, tire, parantez içermez. Sınavların `programs` önekidir. Sınavı olan bölümün kodu değiştirilemez. |
| `name` | Bölüm adı. |
| `language` | `"Türkçe"` ya da `"English"`. |
| `classes` | **İsteğe bağlı (2. aşama).** Bölüm-sınıf etiketlerinin sınıf kısmı, metin listesi: `["1","2","3","4"]`. Boşluk, tire, `?`, parantez olmaz. |

### Bölüm-sınıf (karar ve eşleşme kuralı)

Ayrı bir `classGroups` listesi tutulmaz; bölüm-sınıf, **bölüm kodu + sınıf** ile üretilir:

- Sınavda saklanan değer (`exams[].programs` öğesi): **`"<KOD>-<sınıf>"`**, ör. `"YBS-1"`, `"İŞL-1"`.
- Ekranda gösterilen etiket: tire atılır, **`"YBS1"`**, `"İŞL1"`.
- Sınav formunda her bölümün `classes` değerleri onay kutusu olarak çıkar; ortak ve ÇAP derslerinde birden çok seçilir.
- `classes` yoksa seçenekler sınavlardaki değerlerden türetilir. Eski veride sayı **yarıyıldır** (`"BUS-5"` = 5. yarıyıl → etiket `BUS5`);
  uygulama bunu sınıfa çevirmez, olduğu gibi kullanır. Bir dönemde tek bir anlam (sınıf ya da yarıyıl) kullanılmalıdır;
  yeni dönemlerde sınıf (1–4) önerilir.
- `"<KOD>-?"` (sınıfı bilinmiyor) ve kalıba uymayan değerler saklanır, bölüm sayfasında görünür ama çakışma ve art arda sınav denetimine girmez.
- Bir sınav, `programs` içinde `KOD-` ile başlayan değer varsa o bölümün programında görünür.

## `exams` (her sınav)

| Alan | Zorunlu mu | Biçim / kural | Örnek |
|---|---|---|---|
| `id` | Zorunlu | `exam-<sayı>`, dosyada tek. Yeni sınava en büyük numaranın bir fazlası. | `"exam-6"` |
| `date` | Zorunlu | `YYYY-AA-GG` | `"2027-01-04"` |
| `dateLabel` | Zorunlu | `GG.AA.YYYY` (aynı tarih) | `"04.01.2027"` |
| `day` | Zorunlu | Türkçe gün adı (tarihten hesaplanır): Pazartesi … Pazar | `"Pazartesi"` |
| `start`, `end` | Zorunlu | `SS:DD`, 24 saat; `end` > `start` | `"09:00"`, `"09:50"` |
| `courseCode` | Zorunlu (boş olabilir) | Ders kodu | `"YBS101"` |
| `course` | Zorunlu | Ders adı | `"Programlamaya Giriş"` |
| `programs` | Zorunlu (boş liste olabilir) | Bölüm-sınıf değerleri (yukarıda) | `["YBS-1", "İŞL-1"]` |
| `teacher` | Zorunlu (boş olabilir) | Öğretim elemanı; birden çoksa `", "` ile. Yazım `teacherList[].name` ile aynı olmalı. | `"Ali BAKIN, Zekeriya ŞAHİN"` |
| `totalStudents` | Zorunlu (boş olabilir) | Toplam öğrenci, metin | `"45"` |
| `notes` | Zorunlu (boş liste olabilir) | Kısa notlar | `["90 dakika"]` |
| `rooms` | Zorunlu | Derslikler (aşağıda) | |

Sınavlar tarih, sonra başlangıç saatine göre sıralı yazılır. Bilinmeyen ek alanlar korunur.

### `exams[].rooms` (sınavın derslikleri)

| Alan | Biçim / kural | Örnek |
|---|---|---|
| `room` | Derslik kodu (`rooms[].code` ile aynı yazım); birleşik salon tireyle | `"6A1"`, `"3A5-3A6"` |
| `capacity` | Sınav kapasitesi, metin. Form, derslik listeden seçilince `rooms[].examCapacity`'yi yazar. | `"35"` |
| `students` | Bu derslikteki öğrenci, metin | `"21"` |
| `proctor` | Gözetmen yazımı (aşağıda) | `"Taha Gümüş"` |
| `departments` | Bu derslikteki bölümler ve sayıları | `"YBS 13, İŞL 15"` |

### Gözetmen yazımı (`proctor`)

- `"Gerekmiyor"`: gözetmen yok; dersin hocası girer.
- `"Ad Soyad"`; birden çoksa `"A, B"`. Dersin hocası gözetmense `"Ad Soyad (dersin hocası)"`.
- Aynı kişi her yerde aynı yazılmalı (büyük/küçük harf ve Türkçe karakter farkı tolere edilir).

### Başka birimlere verilen gözetmenlikler

`course` sonu `" (Sağlık Bilimleri Fakültesi)"` ya da `" (Üniversite ortak seçmeli ders)"`; `courseCode`, `teacher`, `totalStudents` boş, `programs` boş liste. `examCount`'a girmez.

## `teacherList` (öğretim elemanı kayıtları, 2. aşama)

Öğretim Üyeleri sekmesindeki “+ Öğretim elemanı ekle” ile yazılır. Sınav formunda öğretim elemanı bu listeden seçilir.

```json
"teacherList": [
 {"name": "Ayşe YILMAZ", "title": "Dr. Öğr. Üyesi", "department": "YBS", "email": "ayse.yilmaz@ornek.edu.tr",
  "unavailable": [{"day": "Salı", "start": "09:00", "end": "12:00", "reason": "izin"}]}
]
```

| Alan | Kural |
|---|---|
| `name` | Zorunlu. Tek kişi (virgül yok), sınavlardaki `teacher` yazımıyla aynı (okul listesindeki gibi soyadı büyük). Tekrarsız (harf farkı gözetilmez). Sınavı olan kişinin adı değiştirilemez, kendisi silinemez. |
| `title` | İsteğe bağlı unvan: `Prof. Dr.`, `Doç. Dr.`, `Dr. Öğr. Üyesi`, `Öğr. Gör.`, … |
| `department` | Bölüm kodu (`departments[].code`) ya da `""`. |
| `email` | İsteğe bağlı. “Değişikliği bildir” taslaklarında `epostalar.json`'dan **önce** bakılır. Sayfada gösterilmez (yalnız düzenleyici listesinde). |
| `unavailable` | İzinli/müsait olmadığı zamanlar; biçim `proctorAvailability` ile aynı (aşağıda). Bu zamana sınav konursa uyarı verilir. |

`teacherList` yoksa öğretim elemanları yalnız sınavlardan türetilir (eski davranış).

## `rooms` (derslik kayıtları, 2. aşama)

Derslikler sekmesindeki “+ Derslik ekle” ile yazılır. Derslik kartları `rooms` ile sınavlardaki dersliklerin **birleşimidir**.

```json
"rooms": [
 {"code": "6A1", "floor": 6, "examCapacity": 33, "fullCapacity": 50},
 {"code": "LAB1", "floor": 4, "examCapacity": 20, "fullCapacity": 25, "note": "Bilgisayar laboratuvarı"}
]
```

| Alan | Kural |
|---|---|
| `code` | Zorunlu, tekrarsız (büyük/küçük harf ve boşluk farkı gözetilmez), virgül yok. Sınavda kullanılan dersliğin kodu değiştirilemez, kendisi silinemez. |
| `floor` | Kat, sayı ya da `null`. `null` ise koddaki baştaki sayıdan türetilir (`7D1` → 7); o da yoksa “Diğer” satırı. |
| `examCapacity` | Sınav (aralıklı oturma) kapasitesi, sayı ya da `null`. |
| `fullCapacity` | Tam (yan yana) kapasite, sayı ya da `null`. `examCapacity`'den küçük olamaz. **Hiçbir zaman aşılamaz.** |
| `note` | İsteğe bağlı not. |

Birleşik salonda (`"3A5-3A6"`) parçaların hepsi kayıtlıysa kapasiteler toplanır.

## `settings` (ayarlar, 2. aşama)

Panel → Ayarlar'dan düzenlenir. Alan yoksa ya da bir değer eksikse varsayılan kullanılır.

```json
"settings": {"proctorThreshold": 30, "capacityStretch": 5, "maxConsecutiveExams": 2, "longExamMinutes": 60, "warnOnly": true}
```

| Alan | Varsayılan | Anlamı |
|---|---|---|
| `proctorThreshold` | `30` | Bir derslikte bu sayıda ya da daha çok öğrenci varsa ve gözetmen yoksa (`"Gerekmiyor"`) uyarı. |
| `capacityStretch` | `5` | Sınav kapasitesinin en çok bu kadar aşılmasına izin: `students > examCapacity + capacityStretch` ise uyarı. `examCapacity` için önce `rooms`, yoksa sınav dersliğinin `capacity` alanı kullanılır. |
| `maxConsecutiveExams` | `2` | Aynı bölüm-sınıfın aynı gün art arda en çok kaç sınavı olabilir. Bir sınavın bitişiyle sonrakinin başlangıcı arasında **10 dakika ya da daha az** varsa (çakışanlar dahil) art arda sayılır. |
| `longExamMinutes` | `60` | Süresi bundan **uzun** olan sınav gözetmen görev sayımında 2 görev, diğerleri 1 görev. |
| `warnOnly` | `true` | `true`: uyarılar kaydı durdurmaz, formda “Yine de kaydet” çıkar. `false`: uyarı varken kayıt yapılmaz. Engeller (aşağıda) her durumda kaydı durdurur. |

## Uyarı kuralları

Sınav formu (alan değiştikçe ve kaydetmeden önce) ve Panel → Kontrol (bütün program) aynı kuralları kullanır.
“Örtüşme” = aynı `date` ve `a.start < b.end && b.start < a.end`. Aynı sınav kendisiyle karşılaştırılmaz.

| Tür | Düzey | Ne zaman |
|---|---|---|
| Bölüm-sınıf | uyarı | Aynı bölüm-sınıf (`programs` değeri, `?` hariç) örtüşen iki sınavda. |
| Öğretim elemanı | uyarı | Aynı öğretim elemanı (virgülle ayrılan adlar) örtüşen iki sınavda; ya da `teacherList[].unavailable`'a göre izinli. |
| Derslik | uyarı | Aynı derslik (birleşik salon parçaları dahil) örtüşen iki sınavda. |
| Kapasite | uyarı | `students > examCapacity + capacityStretch`. |
| Kapasite | **engel** | `students > fullCapacity` (yalnız derslik kaydında tam kapasite varsa). |
| Gözetmen eşiği | uyarı | `students ≥ proctorThreshold` ve derslikte gözetmen yok. |
| Art arda sınav | uyarı | Bir bölüm-sınıfın aynı gün art arda sınav zinciri `maxConsecutiveExams`'ı aşıyor. |
| Gözetmen | **engel** | Gözetmen örtüşen başka sınavda görevli; o saatte kendi dersinin sınavı var; `proctorAvailability`'ye göre izinli; aynı sınavda iki derslikte. (Formda, sınavda zaten kayıtlı gözetmen sınavın gün/saati değişmedikçe yeniden denetlenmez.) |

Engel: hiçbir ayarla kaydedilemez. Uyarı: `warnOnly: true` iken onayla (“Yine de kaydet”) kaydedilir, `false` iken kaydedilmez.
Kayıt anında denetim, GitHub'daki güncel `veri.json` ile bir kez daha yapılır.

## `proctorAvailability` (gözetmen kayıtları)

```json
"proctorAvailability": [
 {"name": "Seda Emir", "email": "seda.emir@ornek.edu.tr", "unavailable": [{"day": "Pazartesi", "reason": "izin"}, {"date": "2027-01-08", "start": "13:00", "end": "17:00", "reason": "toplantı"}]}
]
```

| Alan | Kural |
|---|---|
| `name` | Gözetmen adı, sınavlardaki `proctor` yazımıyla aynı. |
| `email` | İsteğe bağlı (2. aşama). E-posta taslaklarında `epostalar.json`'dan önce bakılır. |
| `unavailable[].day` | Türkçe gün adı; her hafta o gün. |
| `unavailable[].date` | `day` yerine; yalnız o tarih (`YYYY-AA-GG`). |
| `unavailable[].start`, `end` | İsteğe bağlı `SS:DD`; yazılmazsa bütün gün. |
| `unavailable[].reason` | `"izin"` → “o gün izinli”; başka metin → “müsait değil (metin)”. |

Aynı biçim `teacherList[].unavailable` için de geçerlidir. Görevi olan gözetmen silinemez.

## Türetilen alanlar

- **`assignments`**: her derslikteki her gözetmen için bir kayıt (sınav `id` numarası sırasıyla): sınavın `id, date, dateLabel, day, start, end, courseCode, course, programs, teacher, totalStudents`, ardından `examId`, `room`, `roomStudents` (başka birimde `""`), `proctor` (`(dersin hocası)` eki olmadan), `note` (`""`). `"Gerekmiyor"` görev değildir.
- **`teachers`**: sınavlardaki `teacher` değerleri (tekrarsız) + `teacherList` adlarından listede olmayanlar; sıralı.
- **`proctors`**: `assignments`'taki adlar + `proctorAvailability` adlarından listede olmayanlar; sıralı.
- `meta` sayımları bunlardan.
- Görev sayımı (Gözetmenler, Panel, Excel): gözetmenin görevli olduğu her sınav, süresi `longExamMinutes`'ten uzunsa 2, değilse 1.

## `updates` (Son değişiklikler)

En yeni üstte: `{"tarih": "4 Ocak", "tur": "Sınav" | "Saat" | "Derslik" | "Gözetmen", "metin": "...", "examId": "exam-3"}`.
Metin `<Ders adı> sınavına|sınavında|sınavının|sınavı (<Gün> <SS:DD>, <derslik>)` diye başlarsa ders adı sınav kartını açar.
`examId` isteğe bağlıdır. Sitedeki sınav düzenlemesi değişen her tür için en üste otomatik madde ekler.

## `envelopes` (sınav zarfları)

`{"<examId>": {"teslim": {"tarih": ISO, "kim": login} | null, "dolap": "7D1" | "7D2" | "4D2" | null, "bolumOnay": ..., "komisyonOnay": ..., "not": ""}}`.
Kaydı olmayan sınavın zarfı öğretim üyesindedir. Silinen sınavın zarf kaydı da silinir.

## Excel sayfa/sütun eşlemesi (iki yönlü, 3. aşama)

Panel → Veriler'deki “Excel olarak indir” ve Panel → Veri Tablosu'ndaki “Verileri indir / Şablon indir / Verileri yükle”
aynı sayfaları ve **aynı sütun adlarını** kullanır; Veri Tablosu da bu sayfaları gösterir. Yükleme bütün veriyi dosyadakilerle
değiştirir (tek kayıt). Sütun sırası önemsizdir, başlık adı önemlidir (büyük/küçük harf ve Türkçe karakter farkı tolere edilir).
Başlıkta olmayan sütunlar yok sayılır. Boş satırlar atlanır. Hata satırları Excel satır numarasıyla (başlık = 1) gösterilir.

| Sayfa | Sütunlar | veri.json karşılığı |
|---|---|---|
| **Sınavlar** | Sınav no, Tarih, Gün, Başlangıç, Bitiş, Ders kodu, Ders adı, Öğretim elemanı, Bölüm-sınıf, Toplam öğrenci, Derslik, Kapasite, Derslikteki öğrenci, Gözetmen, Derslikteki bölümler, Notlar | `exams` (her sınav-derslik bir satır) |
| **Derslikler** | Kod, Kat, Sınav kapasitesi, Tam kapasite, Not | `rooms` |
| **Öğretim Elemanları** | Ad Soyad, Unvan, Bölüm, E-posta, İzinler | `teacherList` |
| **Gözetmenler** | Ad Soyad, E-posta, İzinler | `proctorAvailability` |
| **Bölümler** | Kod, Ad, Dil, Sınıflar | `departments` |
| **Duyurular** | Tarih, Tür, Metin, Sınav no | `updates` (en yeni üstte) |
| **Program bilgileri** | Alan, Değer (satırlar: Üniversite, Fakülte, Program adı, Dönem) | `meta` (sayfa isteğe bağlı) |

Ayrıntılar:

- **Sınavlar**: “Sınav no” = `id` (`exam-12` ya da `12`). Aynı sınav no'lu satırlar tek sınavın derslikleridir; sınav düzeyindeki
  sütunlar (Tarih, Başlangıç, Bitiş, Ders kodu, Ders adı, Öğretim elemanı, Bölüm-sınıf, Toplam öğrenci, Notlar) bu satırlarda
  aynı olmalı (sonraki satırlarda boş bırakılabilir). **Yeni sınavda Sınav no boş** bırakılır: tarih + saat + ders kodu + ders adı aynı
  olan satırlar birleşir, numara en büyük numaranın bir fazlasından verilir. Tarih `GG.AA.YYYY` (ya da `YYYY-AA-GG`, ya da Excel tarih hücresi);
  saat `SS:DD` (ya da Excel saat hücresi). “Gün” tarihten hesaplanır (yüklemede okunmaz). Bölüm-sınıf virgülle (`YBS-1, İŞL-1`; `YBS1` de kabul edilir);
  Notlar noktalı virgülle. Gözetmen sütunu `proctor` yazımıyla aynı (`Gerekmiyor`, `A, B`, `Ad (dersin hocası)`).
- **İzinler** (Öğretim Elemanları, Gözetmenler): noktalı virgülle ayrılmış maddeler; her madde gün adı ya da tarih (`YYYY-AA-GG`),
  isteğe bağlı saat aralığı ve parantez içinde neden: `Pazartesi; 2027-01-05 09:00-12:00 (toplantı)`. Neden yazılmazsa `"izin"`.
- **E-posta**: yalnız düzenleme yetkisi olanın indirdiği dosyada vardır. Yüklenen dosyada E-posta sütunu hiç yoksa mevcut adresler korunur;
  sütun varsa boş hücre adresi siler.
- Bölümler → Sınıflar virgülle (`1, 2, 3, 4`); Dil `Türkçe` ya da `English`. Duyurular → Tür `Sınav`, `Saat`, `Derslik`, `Gözetmen`.
- Sayılar (kapasite, öğrenci, kat) tam sayı ya da boş.

Doğrulama (yüklemede ve Veri Tablosu kaydında): zorunlu alanlar, tarih/saat biçimi, bitiş > başlangıç, sayılar, tekrarlar;
sınavdaki **öğretim elemanı Öğretim Elemanları sayfasında**, **derslik (birleşik salon parçaları dahil) Derslikler sayfasında**,
**bölüm-sınıf Bölümler sayfasında** (kod ve sınıf) bulunmalı; duyurudaki sınav no Sınavlar'da olmalı. Hata varsa kayıt yapılmaz.
Ardından Kontrol kuralları çalışır: yalnız **bu değişiklikle ortaya çıkan** sorunlar değerlendirilir (engel → kaydedilmez;
uyarı → `warnOnly` açıkken onayla, kapalıyken kaydedilmez). Dosyada olmayan alanlar (`settings`, `envelopes`, bilinmeyen ek alanlar)
mevcut veriden korunur; silinen sınavların zarf kaydı silinir; türetilen alanlar yeniden hesaplanır.

İndirilen dosyadaki **Gözetmen görevleri**, **Gözetmen yükü** ve **Sınav zarfları** sayfaları yalnız bilgi içindir; yüklemede okunmaz.

## `epostalar.json`

```json
{"hocalar": {"Ad SOYAD": "ad.soyad@ornek.edu.tr"}, "gozetmenler": {"Ad Soyad": "ad.soyad@ornek.edu.tr"}}
```

E-posta adresi aranırken sıra: `teacherList[].email` / `proctorAvailability[].email` → `epostalar.json`. Adresler sayfada gösterilmez.

## Örnek (kısaltılmış)

```json
{
 "meta": {"university": "Örnek Üniversitesi", "faculty": "Örnek Fakültesi", "programName": "2026-2027 Güz Final", "period": "4–8 Ocak 2027",
  "examCount": 1, "assignmentCount": 1, "teacherCount": 1, "proctorCount": 1},
 "departments": [{"code": "YBS", "name": "Yönetim Bilişim Sistemleri", "language": "Türkçe", "classes": ["1", "2", "3", "4"]}],
 "exams": [{"id": "exam-1", "date": "2027-01-04", "dateLabel": "04.01.2027", "day": "Pazartesi", "start": "09:00", "end": "09:50",
  "courseCode": "YBS101", "course": "Programlamaya Giriş", "programs": ["YBS-1"], "teacher": "Ayşe YILMAZ", "totalStudents": "32", "notes": [],
  "rooms": [{"room": "6A1", "capacity": "33", "students": "32", "proctor": "Seda Emir", "departments": "YBS 32"}]}],
 "assignments": [{"id": "exam-1", "date": "2027-01-04", "dateLabel": "04.01.2027", "day": "Pazartesi", "start": "09:00", "end": "09:50",
  "courseCode": "YBS101", "course": "Programlamaya Giriş", "programs": ["YBS-1"], "teacher": "Ayşe YILMAZ", "totalStudents": "32",
  "examId": "exam-1", "room": "6A1", "roomStudents": "32", "proctor": "Seda Emir", "note": ""}],
 "teachers": ["Ayşe YILMAZ"],
 "proctors": ["Seda Emir"],
 "updates": [],
 "proctorAvailability": [{"name": "Seda Emir", "unavailable": [{"day": "Cuma", "reason": "izin"}]}],
 "teacherList": [{"name": "Ayşe YILMAZ", "title": "Dr. Öğr. Üyesi", "department": "YBS", "unavailable": []}],
 "rooms": [{"code": "6A1", "floor": 6, "examCapacity": 33, "fullCapacity": 50}],
 "settings": {"proctorThreshold": 30, "capacityStretch": 5, "maxConsecutiveExams": 2, "longExamMinutes": 60, "warnOnly": true}
}
```
