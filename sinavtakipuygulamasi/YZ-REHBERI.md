# Yapay zekâ rehberi: bu uygulamanın verisini okuma ve yazma

Bu belge, bir yapay zekâ oturumunun (ör. Claude Code) bir Sınav Takip Uygulaması klasörünün verisini nasıl okuyup
güncelleyeceğini anlatır. Aynı belge “Uygulama Oluştur” ile her yeni dönem klasörüne kopyalanır. Alanların tam biçimi:
aynı klasördeki **`VERI-BICIMI.md`**.

## 1. Dosyalar

Klasör (ör. `2627guzfinal/`) şunları içerir:

| Dosya | İçerik | Yapay zekâ yazar mı |
|---|---|---|
| `index.html` | Uygulamanın kodu (`sinavtakipuygulamasi/index.html`'in kopyası). | **Hayır.** Yalnız yeni sürüm alınırken kaynaktan aynen kopyalanır. |
| `veri.json` | Bütün dönem verisi: bölümler, sınavlar, kayıtlar, ayarlar, duyurular, zarflar. | Evet (aşağıdaki kurallarla). |
| `kurallar.json` | Programın kurulduğu kurallar (liste: `id, bolum, baslik, aciklama, tur, kapsam, kaynak`). | Yalnız istenirse; döneme özel kararlar `"kapsam": "donem"`. |
| `epostalar.json` | `{"hocalar": {ad: e-posta}, "gozetmenler": {ad: e-posta}}` | İstenirse. |
| `VERI-BICIMI.md`, `YZ-REHBERI.md` | Belgeler. | Hayır. |

Demo klasörü `sinavtakipuygulamasi/`'dir (`veri.json` → `meta.mode: "demo"`); orada `veri.json` boş kalmalıdır.
Gerçek dönem verisi yalnız dönem klasörlerinde tutulur.

## 2. Okuma

1. `veri.json`'u UTF-8 olarak okuyun. Önce `settings`'i varsayılanlarla birleştirin:
   `{"proctorThreshold": 30, "capacityStretch": 5, "maxConsecutiveExams": 2, "longExamMinutes": 60, "warnOnly": true}`.
2. Kayıt listeleri: `departments` (+`classes`), `teacherList`, `rooms`, `proctorAvailability`. Bunlar yoksa eski
   davranış geçerlidir: öğretim elemanları ve derslikler sınavlardan türetilir.
3. `kurallar.json`'daki genel ve döneme özel kuralları okuyun (yerleştirme kararlarında esas alınır).

## 3. Yazma kuralları

- Yazım biçimi: `json.dumps(veri, ensure_ascii=False, indent=1) + "\n"` (UTF-8, `\n`). Alan sırasını koruyun;
  bilmediğiniz alanları silmeyin.
- Yazmadan önce depodaki güncel dosyayı yeniden okuyun (sitede başkası düzenlemiş olabilir); `git log -- <klasör>/veri.json`
  ile “düzenleme:” commit'lerine bakın ve onları ezmeyin.
- Sınav kayıtlarındaki sayılar metin (`"32"`), `rooms` ve `settings` sayıları gerçek sayı (`32`, yoksa `null`).
- Yeni sınav `id`'si: en büyük `exam-N`'in bir fazlası. Sınavlar tarih + başlangıç saatine göre sıralı.
- `day` ve `dateLabel` `date`'ten hesaplanır (`2027-01-04` → `"Pazartesi"`, `"04.01.2027"`).
- `programs`: `"<bölüm kodu>-<sınıf>"`, sınıf o bölümün `classes` listesinden (ör. `"YBS-1"`; ekranda `YBS1`).
- `teacher` ve derslik kodları kayıt listelerindeki yazımla **aynı** olmalı; listede yoksa önce `teacherList` / `rooms`'a ekleyin.
- Türetilen alanları her yazımda yeniden hesaplayın: `assignments`, `teachers`, `proctors`, `meta.examCount`,
  `meta.assignmentCount`, `meta.teacherCount`, `meta.proctorCount` (kural: `VERI-BICIMI.md` → “Türetilen alanlar”).
- Sitede yapılan sınav değişikliklerinde olduğu gibi, programı değiştiren her işlem için `updates` listesinin **en üstüne**
  kısa bir duyuru ekleyin (ör. `{"tarih": "4 Ocak", "tur": "Saat", "metin": "X sınavı (Pazartesi 09:00, 6A1) Salı 10:00'a alındı.", "examId": "exam-3"}`).
- Commit mesajı: `<klasör> düzenleme: <ne yapıldı>` (Türkçe, kısa).

## 4. Kişisel veri: depoya YAZILMAZ

Depo herkese açıktır. **Öğrenci adı, öğrenci numarası, öğrenci listesi, öğrenci–ders eşleşmesi, çakışma çiftleri gibi
kişisel öğrenci verisi hiçbir dosyaya (veri.json, kurallar.json, commit mesajı, belge) yazılmaz.** Yalnız toplam sayılar
(`totalStudents`, derslikteki `students`, `departments: "YBS 13, İŞL 15"`) yazılır. Ortak öğrenci hesabı gerekiyorsa
yerelde yapılır, sonuç yalnız “bu iki sınav çakışmamalı” kararı ve sayılar olarak yansır. Öğretim elemanı ve gözetmenler
için yalnız ad, unvan, bölüm, kurumsal e-posta ve izinli gün/saat tutulur. Şifre ve anahtarlar yazılmaz.

## 5. Sınav yerleştirirken (kurallar.json + settings)

Yeni bir sınavın gün/saat/dersliğini seçerken:

1. `kurallar.json`'daki sert kurallar (`"tur": "sert"`) çiğnenmez; yumuşak kurallar (`"yumusak"`) mümkün olduğunca uygulanır;
   `"kapsam": "donem"` kararları genel kuralların önündedir.
2. Aşağıdaki uyarı kurallarının hiçbiri oluşmamalı. Oluşmak zorundaysa kullanıcıya açıkça söyleyin; **engel** türündekiler asla yazılmaz.
3. Derslik: öğrenci ≤ `examCapacity + capacityStretch` olan en az dersliği seçin; tam kapasite (`fullCapacity`) asla aşılmaz.
   Sığmıyorsa sınavı birden çok dersliğe bölün (`notes`: `"N dersliğe bölündü"`).
4. Derslikteki öğrenci ≥ `proctorThreshold` ise gözetmen yazın (Gözetmen seçiminde en az görevliden başlayın;
   görev sayımı: süre > `longExamMinutes` ise 2 görev).
5. Uzun sınavlarda (`end - start` > 50 dk) notlara `"90 dakika"` gibi süre yazın.

## 6. Uyarı kurallarının tanımı

“Örtüşme”: iki sınav aynı `date` ve `a.start < b.end` ve `b.start < a.end`. Sınav kendisiyle karşılaştırılmaz.

| Tür | Düzey | Koşul | Örnek mesaj |
|---|---|---|---|
| Bölüm-sınıf | uyarı | Aynı `programs` değeri (`-?` hariç) örtüşen iki sınavda | `YBS1 aynı saatte iki sınava giriyor: X (Pazartesi 04.01.2027 09:00–09:50, 6A1) ile çakışıyor.` |
| Öğretim elemanı | uyarı | Aynı ad (`teacher` virgülle bölünür, ad karşılaştırması harf/Türkçe karakter farkına dayanıklı) örtüşen iki sınavda | `Ayşe YILMAZ aynı saatte iki sınavın öğretim elemanı: X (...).` |
| Öğretim elemanı | uyarı | `teacherList[].unavailable` sınavın zamanına denk geliyor | `Ayşe YILMAZ bu sınavın zamanında izinli (Salı 09:00–12:00).` |
| Derslik | uyarı | Aynı derslik kodu (birleşik salon parçaları dahil) örtüşen iki sınavda | `Derslik 6A1 aynı saatte başka bir sınavda: X (...).` |
| Kapasite | uyarı | `students > examCapacity + capacityStretch` | `6A1: 40 öğrenci, sınav kapasitesi 33 + esneme 5 = 38 sınırını aşıyor.` |
| Kapasite | engel | `students > fullCapacity` | `6A1: 55 öğrenci tam kapasiteyi (50) aşıyor; tam kapasite aşılamaz.` |
| Gözetmen eşiği | uyarı | `students ≥ proctorThreshold` ve `proctor` `"Gerekmiyor"` | `6A1: 32 öğrenci var (eşik 30) ama gözetmen yazılmamış.` |
| Art arda sınav | uyarı | Bir bölüm-sınıfın aynı gündeki sınavları başlangıca göre sıralanır; sonraki sınav öncekinin bitişinden en çok 10 dk sonra (ya da örtüşerek) başlıyorsa aynı zincirdedir; zincir uzunluğu > `maxConsecutiveExams` | `YBS1 Pazartesi 04.01.2027 günü art arda 3 sınava giriyor (en çok 2): A 09:00, B 10:00, C 11:00.` |
| Gözetmen | engel | Gözetmen örtüşen başka sınavda görevli / o saatte kendi dersinin sınavı var / `proctorAvailability`'ye göre izinli / aynı sınavda iki derslikte | `Seda Emir o gün izinli (Cuma).` |

`settings.warnOnly` yalnız uyarıları etkiler (`true`: onayla kaydedilebilir, `false`: kaydedilmez); engeller her zaman kaydı durdurur.
Yazdıktan sonra siteyi açıp **Panel → Kontrol**'e bakmak, bütün programın aynı kurallarla taranmış listesini verir
(“Sorun bulunmadı” ya da sorunlar).

## 7. Örnek: yeni sınav ekleme

İstek: “YBS1 ve İŞL1'in ortak dersi Bilişim Teknolojileri, Ayşe YILMAZ, 60 öğrenci, 5 Ocak'ta.”

1. `departments`'ta YBS ve İŞL'nin `classes`'ında `"1"` var → `programs: ["YBS-1", "İŞL-1"]`.
2. `teacherList`'te `Ayşe YILMAZ` var; izinleri Salı 09:00–12:00 → 5 Ocak 2027 Salı ise 13:00 seçilir.
3. 13:00'te YBS-1 ve İŞL-1'in başka sınavı yok, art arda zinciri 2'yi aşmıyor.
4. `rooms`: 6A1 (33/50) ve 6A2 (33/47) o saatte boş → 30 + 30 öğrenci, her ikisi ≥ 30 → iki gözetmen (izinli olmayan, o saatte görevsiz, en az görevli).
5. Kayıt:

```json
{
 "id": "exam-42",
 "date": "2027-01-05",
 "dateLabel": "05.01.2027",
 "day": "Salı",
 "start": "13:00",
 "end": "13:50",
 "courseCode": "ORT101",
 "course": "Bilişim Teknolojileri",
 "programs": ["YBS-1", "İŞL-1"],
 "teacher": "Ayşe YILMAZ",
 "totalStudents": "60",
 "notes": ["2 dersliğe bölündü"],
 "rooms": [
  {"room": "6A1", "capacity": "33", "students": "30", "proctor": "Seda Emir", "departments": "YBS 30"},
  {"room": "6A2", "capacity": "33", "students": "30", "proctor": "Taha Gümüş", "departments": "İŞL 30"}
 ]
}
```

6. Türetilen alanları yeniden hesaplayın, `updates`'in en üstüne
   `{"tarih": "<bugün>", "tur": "Sınav", "metin": "Bilişim Teknolojileri sınavı (Salı 13:00, 6A1, 6A2) programa eklendi (gözetmen: Seda Emir, Taha Gümüş).", "examId": "exam-42"}`
   ekleyin ve `<klasör> düzenleme: Bilişim Teknolojileri eklendi` mesajıyla commit edin.

## 8. Örnek: kayıt ekleme

```json
"teacherList": [..., {"name": "Mehmet KAYA", "title": "Öğr. Gör.", "department": "İŞL", "unavailable": [{"date": "2027-01-07", "reason": "konferans"}]}],
"rooms": [..., {"code": "4D2", "floor": 4, "examCapacity": 24, "fullCapacity": 36}],
"proctorAvailability": [..., {"name": "Elif Nur Eken", "unavailable": [{"day": "Çarşamba", "start": "13:00", "end": "17:00", "reason": "izin"}]}]
```

Boş e-postayı (`""`) yazmak yerine alanı hiç yazmamak tercih edilir. Kayıt eklendikten sonra `teachers` / `proctors`
türetilen listelerini ve `meta` sayımlarını güncelleyin.
