# veri.json biçimi

Deneme sürümü (v2, https://iybf-sinav.github.io/v2/) sınav programını sayfanın içinden değil **`v2/veri.json`** dosyasından okur. Tasarım (`v2/index.html`) ile veri ayrıdır: komisyonun programı yalnız bu dosyayı üretir, sitenin tasarımında yapılan değişiklikler veri güncellemelerinde silinmez.

- Dosya UTF-8'dir; Türkçe harfler olduğu gibi yazılır (`ensure_ascii=False`).
- Python'da şöyle yazılır: `json.dumps(veri, ensure_ascii=False, indent=1) + "\n"`. Sitedeki “Düzenle” özelliği de dosyayı aynı biçimde geri yazar; böylece GitHub'daki farkta yalnız değişen satırlar görünür.
- Bütün sayılar (öğrenci, kapasite) **metin** olarak yazılır: `"21"`, bilinmiyorsa `""`. Yalnız `meta` içindeki sayımlar gerçek sayıdır.

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
 "proctorAvailability": [ ... ]
}
```

| Alan | Zorunlu mu | Ne işe yarar |
|---|---|---|
| `meta` | Zorunlu | Kurum, dönem ve sayımlar (sayfa başlıklarındaki “120 sınav · 2–6 Kasım 2026” gibi yazılar). |
| `departments` | Zorunlu | Sınav Programları sayfasındaki bölüm düğmeleri. |
| `exams` | Zorunlu | Asıl veri: her sınav bir kayıt. |
| `assignments` | Zorunlu (türetilir) | Gözetmen görevleri; `exams`'ten hesaplanır. |
| `teachers` | Zorunlu (türetilir) | Öğretim Üyeleri sayfasındaki isimler; `exams`'ten hesaplanır. |
| `proctors` | Zorunlu (türetilir) | Gözetmenler sayfasındaki isimler; `assignments`'tan hesaplanır. |
| `updates` | İsteğe bağlı | Ana Sayfa'daki “Son değişiklikler” kutusu. Yoksa ya da boşsa kutu görünmez. |
| `proctorAvailability` | İsteğe bağlı | Gözetmenlerin izinli / müsait olmadığı gün ve saatler. “Düzenle” bu günlere gözetmen atanmasını engeller. Yoksa ya da boşsa yalnız saat çakışması denetlenir. |

“Türetilir” denen alanlar elle yazılmaz; `8_site_uret.py` (`veri_kur`) ve sitedeki “Düzenle” özelliği bunları sınavlardan aynı kuralla yeniden hesaplar.

## `meta`

| Alan | Örnek | Açıklama |
|---|---|---|
| `institution` | `"İstanbul Esenyurt Üniversitesi"` | Kurum adı. |
| `faculty` | `"İşletme ve Yönetim Bilimleri Fakültesi"` | Fakülte adı. |
| `period` | `"2–6 Kasım 2026"` | Sınav haftası (araya uzun tire `–`). |
| `examCount` | `120` | İYBF sınavlarının sayısı; başka birimlere verilen gözetmenlik kayıtları (aşağıda) sayılmaz. |
| `assignmentCount` | `90` | `assignments` uzunluğu. |
| `teacherCount` | `45` | `teachers` uzunluğu. |
| `proctorCount` | `14` | `proctors` uzunluğu. |

## `departments`

Her bölüm: `{"code": "SBUİ", "name": "Siyaset Bilimi ve Uluslararası İlişkiler", "language": "Türkçe"}`. Hepsi zorunlu. `language` `"Türkçe"` ya da `"English"`. Sıra, sayfadaki düğme sırasıdır. Bir sınav, `programs` alanında `KOD-` ile başlayan bir program varsa o bölümde görünür.

Kodlar: SBUİ, PSIR, İŞL, BUS, UTF, LOJ, HAV, YBS, ECF, ETİC.

## `exams` (her sınav)

| Alan | Zorunlu mu | Biçim / kural | Örnek |
|---|---|---|---|
| `id` | Zorunlu | `exam-<sayı>`, dosyada tek. Yeni sınava en büyük numaranın bir fazlası verilir. | `"exam-6"` |
| `date` | Zorunlu | `YYYY-AA-GG` | `"2026-11-02"` |
| `dateLabel` | Zorunlu | `GG.AA.YYYY` (aynı tarih) | `"02.11.2026"` |
| `day` | Zorunlu | Türkçe gün adı, büyük harfle başlar: Pazartesi, Salı, Çarşamba, Perşembe, Cuma | `"Pazartesi"` |
| `start` | Zorunlu | `SS:DD`, 24 saat, başında sıfır | `"09:00"` |
| `end` | Zorunlu | `SS:DD`; 50 dakikalık sınavda `:50`, uzun sınavda gerçek bitiş (ör. `10:30`) | `"11:50"` |
| `courseCode` | Zorunlu (boş olabilir) | Ders kodu; yoksa `""` | `"2016G4001"` |
| `course` | Zorunlu | Ders adı | `"Siyaset Psikolojisi"` |
| `programs` | Zorunlu (boş liste olabilir) | `BÖLÜMKODU-dönem` listesi; dönem bilinmiyorsa `?` | `["BUS-1", "ECF-3"]`, `["YBS-?"]` |
| `teacher` | Zorunlu (boş olabilir) | Öğretim elemanı; birden çoksa virgül ve boşlukla, alfabetik. Soyadı büyük harfle (okul listesindeki gibi) | `"Ali BAKIN, Zekeriya ŞAHİN"` |
| `totalStudents` | Zorunlu (boş olabilir) | Toplam öğrenci, metin | `"45"` |
| `notes` | Zorunlu (boş liste olabilir) | Kısa notlar | `["2 dersliğe bölündü", "90 dakika"]` |
| `rooms` | Zorunlu | Derslikler (aşağıda) | |

Sınavlar tarih, sonra başlangıç saatine göre sıralı yazılır.

Kullanılan notlar: `"N dersliğe bölündü"` (birden çok derslik varsa), `"60 dakika"` / `"90 dakika"` / `"120 dakika"` (50 dakikadan uzunsa), başka birim kayıtlarında `"Başka fakülte: İYBF'den verilen gözetmen"` ya da `"Üniversite ortak seçmeli: İYBF'den verilen gözetmen"`.

### `rooms` (her derslik)

| Alan | Biçim / kural | Örnek |
|---|---|---|
| `room` | Derslik adı | `"6A1"`, birleşik salon `"3A5-3A6-3D6-3D7"` |
| `capacity` | Sınav kapasitesi, metin; bilinmiyorsa `""` | `"35"` |
| `students` | Bu derslikteki öğrenci, metin | `"21"` |
| `proctor` | Gözetmen yazımı (aşağıda) | `"Taha Gümüş, Tunahan Başoğlu"` |
| `departments` | Bu derslikteki bölümler ve öğrenci sayıları, `KOD sayı` virgülle | `"ECF 13, PSIR 15"` |

Derslik sırası: önce 3. kat derslikleri (3 ile başlayanlar), sonra diğerleri, her grup kendi içinde alfabetik (`8_site_uret.py` ile aynı).

### Gözetmen yazımı (`proctor`)

- **`"Gerekmiyor"`**: gözetmen gerekmiyor; sitede “Dersin hocası (gözetmen gerekmiyor)” olarak görünür.
- **`"Ad Soyad"`**: gözetmenin adı, normal yazımla (yalnız ilk harfler büyük): `"Merve Sevinç Sakar"`.
- **`"Ad Soyad (dersin hocası)"`**: dersin hocası kendi sınavında gözetmen sayılıyorsa: `"Duygu Yayla Eldem (dersin hocası)"`. Görev listesine adı ekin olmadan, `"Duygu Yayla Eldem"` olarak girer.
- **Birden çok gözetmen**: virgül ve boşlukla: `"Kadriye Giray, Elif Nur Eken"`.
- Aynı kişi her yerde aynı yazılmalı; yoksa Gözetmenler sayfasında iki ayrı kişi gibi görünür.

### Örnek sınav kaydı

```json
{
 "id": "exam-5",
 "date": "2026-11-02",
 "dateLabel": "02.11.2026",
 "day": "Pazartesi",
 "start": "11:00",
 "end": "11:50",
 "courseCode": "2075B1003",
 "course": "Information and Communication Technologies",
 "programs": ["BUS-1", "ECF-3", "PSIR-1"],
 "teacher": "Jumana ALHALİSİ",
 "totalStudents": "45",
 "notes": ["2 dersliğe bölündü"],
 "rooms": [
  {"room": "6D1", "capacity": "17", "students": "17", "proctor": "Mehmet Deniz Nalbantoğlu", "departments": "BUS 17"},
  {"room": "6D5", "capacity": "23", "students": "28", "proctor": "Tunahan Başoğlu", "departments": "ECF 13, PSIR 15"}
 ]
}
```

(Dosyada her alan kendi satırındadır; burada kısaltıldı.)

### Başka birimlere verilen gözetmenlikler

Sağlık Bilimleri Fakültesi ve üniversite ortak seçmeli derslerine İYBF'den verilen gözetmenler de sınav kaydı olarak girer: `course` sonunda `" (Sağlık Bilimleri Fakültesi)"` ya da `" (Üniversite ortak seçmeli ders)"`, `courseCode`, `teacher`, `totalStudents` boş, `programs` boş liste, derslikte `capacity` ve `students` boş, `departments` birimin adı. Bu kayıtlar `examCount`'a girmez.

## Türetilen alanlar

- **`assignments`**: her derslikteki her gözetmen için bir kayıt; sınavlar `id` numarası sırasıyla. Alanlar: sınavın `id, date, dateLabel, day, start, end, courseCode, course, programs, teacher, totalStudents`, ardından `examId` (= `id`), `room`, `roomStudents` (derslikteki öğrenci; başka birim kaydında `""`), `proctor` (`(dersin hocası)` eki olmadan), `note` (`""`). `"Gerekmiyor"` görev sayılmaz.
- **`teachers`**: sınavlardaki `teacher` değerleri, tekrarsız ve sıralı (boşlar hariç).
- **`proctors`**: `assignments`'taki gözetmen adları, tekrarsız ve sıralı.

## `updates` (Son değişiklikler)

`kod/Yöntem/degisiklikler.json` ile aynı biçim; **en yeni üstte**:

```json
"updates": [
 {"tarih": "2 Kasım", "tur": "Gözetmen", "metin": "Economics of Development sınavına (Pazartesi 13:00, 6D1) gözetmen olarak Merve Sevinç Sakar eklendi."}
]
```

- `tarih`: duyuru günü, `"G Ay"` (ör. `"2 Kasım"`). İlk maddenin tarihindeki maddeler açık görünür; daha eskiler “Önceki değişiklikler (N)” altında kapalı durur.
- `tur`: `"Sınav"` ya da `"Gözetmen"` (rozet rengi buna göre).
- `metin`: düz metin. Site maddeyi sınavla eşleştirip altına güncel gün, saat, derslik, gözetmen ve öğretim elemanını ekler. Bunun için metin şöyle başlamalı: **`<Ders adı> sınavına (<Gün> <SS:DD>, <derslik>[, <derslik>])`**, ör. `Economics of Development sınavına (Pazartesi 13:00, 6D1) ...`. Eşleşmeyen madde olduğu gibi gösterilir.

## `proctorAvailability` (gözetmen izin günleri)

Her gözetmen için bir kayıt; yalnız ad ve izinli gün/saat yazılır (başka kişisel bilgi yazılmaz):

```json
"proctorAvailability": [
 {"name": "Melih Mert Oskay", "unavailable": [{"day": "Salı", "reason": "izin"}]},
 {"name": "Seda Emir", "unavailable": [{"day": "Pazartesi", "reason": "izin"}, {"day": "Cuma", "reason": "izin"}]}
]
```

| Alan | Biçim / kural |
|---|---|
| `name` | Gözetmen adı, sınavlardaki `proctor` yazımıyla aynı (büyük/küçük harf ve Türkçe karakter farkı tolere edilir). |
| `unavailable[].day` | Türkçe gün adı (`"Salı"`); her hafta o gün. `date` yazılırsa yerine yalnız o tarih (`"2026-11-03"`) geçer. |
| `unavailable[].start`, `end` | İsteğe bağlı, `SS:DD`. Yazılmazsa bütün gün; yazılırsa yalnız o saat aralığı. |
| `unavailable[].reason` | `"izin"` → “X o gün izinli (Salı).”; başka bir metin → “X o gün müsait değil (Salı: metin).” |

Kaynak (Kasım 2026 vizesi): `kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx` → “Gözetmen Yükü” sayfası, “İzin günü / kısıt” sütunu (aynı bilgi `kod/Belgeler/Devir Notu.md`'de). `esitle.py` ana sitede bu alan yoksa v2'deki listeyi korur.

### “Düzenle”deki gözetmen denetimi

Kaydetmeden önce (ve gözetmen, tarih, saat alanı değiştikçe) girilen her gözetmen için şunlar denetlenir; biri bile varsa kayıt yapılmaz:

- Aynı gün, saat aralığı örtüşen başka bir sınavda gözetmen mi?
- O saatte kendi dersinin sınavı var mı (`teacher` alanında adı geçiyor mu)?
- `proctorAvailability`'ye göre o gün/saat izinli mi?
- Aynı sınavda iki derslikte birden yazılmış mı?

Aynı sınavın kendisi çakışma sayılmaz. Sınavda zaten kayıtlı olan bir gözetmen, sınavın gün/saati değişmedikçe yeniden denetlenmez (komisyonun bilerek yaptığı atamalar düzenlemeyi kilitlemesin); gün/saat değişirse bütün gözetmenler yeni zamana göre denetlenir. Denetim GitHub'daki güncel veri.json'la kayıt anında bir kez daha yapılır.

## Gizli bilgiler: `gizli.json` (özel depo)

Panel şifresi **bu herkese açık depoya, sitenin koduna ya da `veri.json`'a yazılmaz.** Düzenleyici girişi yapılmışken site şifreyi, düzenleyicinin GitHub anahtarıyla, **özel** `iybf-sinav/iybf-gizli` deposundaki `gizli.json` dosyasından okur (`GET https://api.github.com/repos/iybf-sinav/iybf-gizli/contents/gizli.json`). Okunan şifre yalnız tarayıcının belleğinde ve, panelin kendisi gibi, o sekmenin oturumunda (`sessionStorage` `panel_sifre`) tutulur; localStorage'a yazılmaz, “Çıkış”ta silinir.

Biçim (değer örnektir, uydurmadır):

```json
{"panelSifresi": "örnek-şifre"}
```

- `panelSifresi`: Panel sekmesi açılınca panele verilir, panel şifre sormadan açılır (Değişiklik 10). Yoksa ya da dosya okunamazsa panel kendi şifre ekranıyla açılır.

**Kim, nasıl oluşturur:** depo sahibi (iybf-sinav hesabı) GitHub'da **Private** (özel) bir `iybf-gizli` deposu açar, içine yukarıdaki biçimde `gizli.json` dosyasını ekler ve düzenleyicileri bu depoya da ortak (collaborator) yapar. Düzenleyicinin klasik anahtarındaki `repo` kapsamı özel depoyu okumaya yeter. Panel şifresi `kod/Yöntem/panel_sifre.txt`'deki şifredir (o dosya da GitHub'a yüklenmez).

## Siteye nasıl gelir

- v2'de: depo kökünden `python3 v2/esitle.py`. Kökte `veri.json` varsa onu, yoksa ana sitenin (`index.html`) gömülü verisini ve `kod/Yöntem/degisiklikler.json`'u okuyup `v2/veri.json`'u yazar. **Dikkat:** v2'de “Düzenle” ile yapılan değişiklikler bu sırada ana sitenin verisiyle değişir.
- Sitedeki “Düzenle” özelliği yalnız `v2/veri.json`'u değiştirir (commit mesajı `v2 düzenleme: ...`).

---

## Depo sahibi için: Claude oturumuna yapıştırılacak talimat

Aşağıdaki metni olduğu gibi kendi Claude oturumunuza yapıştırabilirsiniz.

```text
iybf-sinav.github.io deposunda komisyonun Python motoru kod/Yöntem/kod/8_site_uret.py siteyi
(Sınav Çıktıları/GitHub Pages/Liste N/index.html) üretiyor. Şunu istiyorum:

1. 8_site_uret.py siteyi üretirken aynı veriyi index.html'nin yanına veri.json olarak da yazsın
   (sitenin kökünde, index.html ile aynı klasöre konacak). Mevcut çıktıları DEĞİŞTİRME: index.html
   bugünkü gibi, gömülü verisiyle aynen üretilmeye devam etsin; yalnız ek bir dosya yazılsın.
2. veri.json içeriği: veri_kur(...) döndürdüğü sözlük (meta, departments, exams, assignments,
   teachers, proctors; alan sırası aynı) + sonuna "updates": Yöntem/degisiklikler.json'daki liste
   (her öğe {"tarih", "tur", "metin"}, en yeni üstte; dosya yoksa boş liste).
3. Yazım: json.dumps(veri, ensure_ascii=False, indent=1) + "\n", UTF-8, satır sonu "\n"
   (open(..., "w", encoding="utf-8", newline="\n")). Biçim kuralları v2/VERI-BICIMI.md'de.
4. Değişikliği küçük tut, Türkçe kısa yorum yaz; çalıştırıp veri.json'un index.html'deki
   gömülü veriyle (updates hariç) aynı olduğunu doğrula.

UYARI — motoru çalıştırmadan önce: sitede GitHub üzerinden elle düzenleme yapılmış olabilir
(v2'deki "Düzenle" özelliği v2/veri.json'a "v2 düzenleme: ..." mesajıyla commit atar; ileride
kökteki veri.json da elle düzenlenebilir). Motoru çalıştırmadan önce depodaki güncel veri.json'u
(kökte ve v2/ altında) ve git log'daki "düzenleme" commit'lerini kontrol et; motorun Excel
kaynaklarında olmayan bir değişiklik varsa bana göster ve önce kaynaklara işle. Yoksa yeni üretilen
veri.json bu elle düzenlemelerin üzerine yazar ve onları siler.
```
