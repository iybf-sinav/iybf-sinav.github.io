# Boş şablon: yeni dönem nasıl açılır

Bu klasör sınav programı sitesinin boş kopyasıdır (sınav yok, yalnız 10 bölüm). Kod klasör adına bağlı değildir:
düzenlemeler sayfanın bulunduğu klasörün `veri.json`'una yazılır, başlık ve sekme adı `veri.json` → `meta`'dan gelir.

1. **Kopyala ve adlandır:** `bossablon/` klasörünü depo kökünde yeni adla kopyalayın (ör. `2728vizeprogrami/`).
   `index.html`'e dokunmayın.
2. **meta'yı doldurun** (`veri.json`):
   - `programName`: başlıkta ve sekme adında görünen ad, ör. `"2027-2028 Güz Dönemi Vize"`
     (alt satır: "<programName> Sınav Takip Uygulaması · <period>").
   - `period`: sınav tarihleri, ör. `"1–5 Kasım 2027"` (bilinmiyorsa `""` bırakın).
   - `faculty`, `institution`: gerekirse; sayılar (`examCount` vb.) kayıtta kendiliğinden güncellenir.
   - `departments`: bölüm listesi değiştiyse güncelleyin.
3. **Sınavları ekleyin:** ya sitede "Düzenleyici girişi" → Sınav Programları → "Yeni sınav ekle"
   (ilk sınavda tarihi "Başka tarih…" ile girin; sonra program günleri listede çıkar), ya da yerleştirme
   motorunun çıktısını (`exams`, `proctorAvailability`, `updates`; biçim: kökteki `VERI-BICIMI.md`) `veri.json`'a koyun.
   Gün sütunları ve saatler veriden türetilir.
4. İsteğe bağlı: `epostalar.json`'a hoca/gözetmen e-postaları, `kurallar.json`'a döneme özel kurallar (`"kapsam": "donem"`).

Kökteki `index.html` yönlendirmesini yeni klasöre çevirmek ayrı bir karardır; bu adımlar onu değiştirmez.
