# Devir Notu: İYBF Sınav Sitesi ve Sınav Takip Uygulaması

*Son güncelleme: 5 Kasım 2026. Bu dosya yeni bir Claude oturumunun kaldığı yerden devam etmesi içindir.*

**Yeni oturuma ilk komut:** "DEVIR-NOTU.md'yi oku ve bana kısa bir özet geç."

---

## 1. Kim, ne, nerede

- **Kullanıcı:** İYBF (İstanbul Esenyurt Üniversitesi, İşletme ve Yönetim Bilimleri Fakültesi) Sınav Planlama Komisyonu'ndan.
  - Türkçe konuşur, kısa ve az iş çıkaran çözümleri tercih eder, token tasarrufuna önem verir.
  - Teknik ayrıntıdan çok sonucu ister.
- **Depo:** GitHub `iybf-sinav/iybf-sinav.github.io`, GitHub Pages ile yayında. Bütün iş bu depoda.
  - Eski kod deposu `0ISKA0/sinav-programi-kod` artık kullanılmıyor; kodlar `kod/` klasörüne taşındı.
- **Depo sahibi** ayrı bir kişi. Kendi Claude oturumuyla `kod/` (Python motoru), `panel/` ve canlı veriyi günceller.
  - Commit'leri "0ISKA0" ya da "Melih Mert Oskay" adıyla görünür.
  - Sahibin dosyalarına dokunurken dikkat et.
- **Çalışma dalı:** `claude/friendly-ride-xyqg5r`.
  - Kullanıcı `main`'e doğrudan yayın izni verdi.
  - İzin şunları kapsar: `sinavtakipuygulamasi/`, `2627vizeprogrami/v2/` ve kendi istediği canlı değişiklikler.

## 2. Klasör düzeni (adresler)

| Klasör | Adres | Ne |
|---|---|---|
| `index.html` (kök) | https://iybf-sinav.github.io | Yalnız yönlendirme → `/2627vizeprogrami/`. Üzerine site YAZILMAZ. |
| `2627vizeprogrami/` | …/2627vizeprogrami/ | **CANLI** 2026-27 Güz vize programı. Herkes kullanıyor; kullanıcı açıkça istemedikçe DOKUNMA. Veri `veri.json`, düzenlemeler buraya yazılır. Görünüşü 3 Kasım'daki kök siteyle aynı; sonradan yalnız Panel'e "Excel olarak indir" eklendi. Şablonu `kod/Yöntem/site_tasarimi.html` (birebir aynı tutulur). |
| `2627vizeprogrami/v2/` | …/2627vizeprogrami/v2/ | Eski deneme sürümü (Değişiklik 1–8: derslikler, zarf uygulaması, kurallar, panel şifre kapısı vb.). Artık ana geliştirme burada DEĞİL. |
| `sinavtakipuygulamasi/` | …/sinavtakipuygulamasi/ | **ANA GELİŞTİRME YERİ.** Genel amaçlı "Sınav Takip Uygulaması" (her üniversite/fakülte kullanabilir). Kendisi DEMO'dur. |
| `panel/` | …/panel/ | Sahibin şifreli komisyon paneli. DOKUNMA. |
| `kod/` | — | Sahibin Python motoru, belgeleri, Excel'leri. `kod/OKU-BENI.md` klasör düzenini anlatır. |
| `bossablon/`, `v2/` | — | Yalnız yönlendirme sayfaları. |

## 3. Sınav Takip Uygulaması (sinavtakipuygulamasi/)

- **Dosyalar:**
  - `index.html`: bütün uygulama, tek dosya, ~4–5 bin satır.
  - `veri.json`: demoda `meta.mode: "demo"`.
  - `epostalar.json`, `kurallar.json`: genel kurallar.
  - `VERI-BICIMI.md`: tam veri biçimi ve Excel sütun eşlemesi.
  - `YZ-REHBERI.md`: bir yapay zekâ oturumunun veriyi nasıl okuyup yazacağı, yerleştirme yapıp Excel'le yükleyeceği.
  - `OKU-BENI.md`.
- **Demo modu:**
  - Herkes düzenleyebilir; kayıt yalnız tarayıcıda (localStorage `sinav-takip-demo:<klasör>`).
  - Üstte DEMO şeridi var: "Örnek veriyle doldur" ve "Demo verisini sıfırla".
- **Gerçek mod (oluşturulan dönemler):**
  - Düzenleme yalnız "Düzenleyici girişi" ile yapılır: GitHub klasik token, `repo` kapsamı, localStorage'da tutulur.
  - Kayıt GitHub Contents API ile klasörün kendi `veri.json`'una gider.
  - Kayıt katmanı tek yerde: `loadDoc`/`saveDoc`. Demoda localStorage, gerçekte `commitFile`.
- **Uygulama Oluştur:**
  - Yalnız düzenleyici girişiyle çalışır.
  - Sorduğu bilgiler: üniversite, fakülte, dönem adı, tarihler, adres uzantısı.
  - Git Data API ile tek commit'te yeni klasör kurar: index.html, boş veri.json, kurallar, belgeler.
- **Bu dönemi sil:**
  - Panel > Veriler'de, kırmızı uyarıyla; dönem adının yazılması gerekir.
  - Korumalı klasörler silinemez.
- **Özellikler:**
  - İki uygulama: Sınav Programı / Sınav Zarfları. Zarf takibinde 3 adım ve dolaplar (7D1, 7D2, 4D2) var.
  - Kayıtlar: sınav, öğretim elemanı (`teacherList`), derslik (`rooms`), bölüm ve sınıflar (`departments[].classes`, sınavda `programs: ["YBS-1"]`), gözetmen ve izinler (`proctorAvailability`), duyurular (`updates`), kurallar, ayarlar (`settings`).
  - Uyarılar: sınıf, hoca, derslik ve gözetmen çakışması; kapasite; izin; art arda sınav; gözetmen eşiği. `settings.warnOnly` ile "uyar" ya da "engelle". Tam kapasite aşımı ve gözetmen çakışması/izni her zaman engellenir.
  - Panel alt sekmeleri: Veriler | Kurallar | Ayarlar | Kontrol (bütün programı tarar) | Veri Tablosu (Excel benzeri düzenleme, Excel indir/yükle/şablon).
  - Yazdır/PDF görünümleri, gözetmen görev çizelgesi, takvimi PNG indirme, takvimde parmakla yakınlaştırma.
- **Son yapılan (5 Kasım):**
  - Düzenleyici girişi footer'a taşındı.
  - Footer'da "Normal görünüm | Düzenleyici görünümü" seçicisi eklendi.
  - Sağ altta "Kendi uygulamanı oluştur" düğmesi ve açılır penceresi eklendi.
- **Görev sayımı kuralı (komisyon):** 60 dk'dan uzun sınav 2 görev sayılır, kendi dersindeki gözetmenlik dahil (`settings.longExamMinutes`).

## 4. Önemli kararlar ve kurallar

- **Canlı site** (`2627vizeprogrami/`): Ziyaretçi dün ne gördüyse bugün de onu görmeli. Değişiklik ancak kullanıcı açıkça isterse yapılır.
- **Öğrenci verisi:** Kişisel öğrenci verisi (T.C. no, öğrenci no, ad) hiçbir zaman depoya yazılmaz. Yerleştirme için gerekirse kullanıcı dosyayı doğrudan Claude oturumuna atar.
- **E-postalar:** Kurumsal e-postalar depoda açık durabilir, ama sitede görünür gösterilmez; yalnız düzenleyiciye ve mailto bağlantısında.
- **Şifreler:** Panel şifresi koda/depoya yazılmaz. v2'deki panel kapısı şifreyi, sahibin panel verisini çözmeyi deneyerek doğrular.
- **Sahibin motoru:** Sahip motoru çalıştırınca `2627vizeprogrami/veri.json`'u yeniden yazar. Siteden yapılan düzenlemeler sahibin Excel'ine işlenmemişse kaybolabilir (kodda not var). Sınav Takip Uygulaması'nda bu sorun yok: veri doğrudan sitede yönetilir.
- **Yapay zekâ isteğe bağlı:** Her şey elle yapılabilmeli. Yapay zekâ `kurallar.json` + `settings` + `YZ-REHBERI.md`'ye göre yerleştirme yapıp Excel biçiminde verebilir.
- **Kural derlemesi:** 171 kural `2627vizeprogrami/v2/kurallar.json` ve `KURALLAR.md`'de. Bunlardan 20'si "Çelişkiler", 15'i "Finalde sorulacaklar".

## 5. Çalışma yöntemi ve tasarruf

- **Kullanıcının isteği:** Orkestra şefi gibi çalış, işleri alt ajanlara ver, kontrol et. Ama kullanım sınırı çabuk doluyor.
- **Bu oturumda öğrenilenler:**
  - Tek büyük `index.html` her işte yeniden okunuyor: pahalı.
  - Paralel ajanlar sınırı hızla dolduruyor; sırayla çalıştır.
  - Testleri temel senaryolarla, az ekran görüntüsüyle sınırla.
- **Önerilen sonraki adımlar** (kullanıcı onaylamadı, sor):
  1. `sinavtakipuygulamasi/index.html`'i birkaç dosyaya bölmek (css/görünüm/veri/düzenleme/panel). Ajanlar yalnız ilgili parçayı okur.
  2. Rutin işler için daha hafif model (Agent `model: "sonnet"`).
- **Test ortamı:**
  - Depo kökünden `python3 -m http.server` + Playwright (`require('playwright')`, `chromium.launch()`).
  - cdnjs bu ortamda engelli: SheetJS/html2canvas için `npm pack` yerel kopyası + `page.route`.
  - GitHub API `page.route` ile taklit edilir.
- **GitHub push:** Ara sıra geçici "Internal Server Error" verir; 2/4/8/16 sn bekleyip yeniden dene. Kullanıcı açıkça istemedikçe `main`'e push etme.
- **Commit mesajları:** Sonuna şu iki satır eklenir:
  ```
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_0146MiFWW1RtotjbcFyt7WWm
  ```
  Yeni oturumda kendi oturum bağlantını kullan.

## 6. Açık konular

- "Uygulama Oluştur" ve "Bu dönemi sil" gerçek GitHub'da denenmedi; yalnız taklit API ile test edildi. Kullanıcıdan bir deneme dönemi oluşturup silmesini iste.
- Oluşturulan dönem klasörlerindeki `index.html` kendiliğinden güncellenmez. Yeni sürüm gelince eski dönemlerin index.html'i elle değiştirilmeli. İleride "uygulamayı güncelle" düğmesi düşünülebilir.
- Uygulamada hâlâ birkaç İYBF'ye özgü iz olabilir: "Uygulama hakkında" metni, kurallar.json'daki bazı genel kurallar. Genelleştirme gerekebilir.
- Veri Tablosu kaydı bütün veriyi yazar. Aynı anda iki kişi düzenlerse son kaydeden kazanır.
- `2627vizeprogrami/` canlı sitesinde Kontrol benzeri bir tarama 35 olası sorun gösterdi: 15 gözetmen eşiği, 9 kapasite, 2 izinli gözetmen vb. Bilgi olarak kullanıcıya söylendi.
