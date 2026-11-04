# İYBF Sınav Programı: kodlar ve notlar

Bu klasör sayfayı üreten kodların güncel kopyasıdır (2 Kasım 2026).

## Klasör düzeni (4 Kasım 2026'dan itibaren)
- `2627vizeprogrami/` : 2026-2027 Güz vize programı (canlı sayfa). `index.html`, `veri.json`, `epostalar.json` burada. Siteden yapılan düzenlemeler `2627vizeprogrami/veri.json`'a yazılır.
- `2627vizeprogrami/v2/` : geliştiricilerin deneme sürümü.
- `2627finalprogrami/` : final programı (hazırlanıyor). `bossablon/` : yeni dönem için boş şablon.
- Kökteki `index.html` yalnız `2627vizeprogrami/`'ye YÖNLENDİRİR; üzerine site YAZMAYIN. Eski `v2/` adresi de yeni yere yönlendirir.
- `panel/` kökte kalır (bütün dönemler `../panel/` ile açar).

## Sayfa nasıl üretilir
1. `Yöntem/kod/7_gozetmenlik_formati.py` gözetmen kişi dosyalarını yazar.
2. `Yöntem/kod/9_panel_uret.py` şifreli panel sayfasını üretir (`panel/index.html` olarak yüklenir).
3. `Yöntem/kod/8_site_uret.py` ana sayfayı üretir (`index.html` olarak yüklenir).
4. Üretilen dosyalar `2627vizeprogrami/index.html`, `2627vizeprogrami/veri.json` ve `panel/index.html` yerine konur ve yüklenir (kökteki `index.html` yönlendirmedir, ona dokunulmaz). `2627vizeprogrami/index.html`'de iki yol farklıdır: `EDIT_FILE = "2627vizeprogrami/veri.json"` ve `PANEL_URL = "../panel/?v=…"` (`Yöntem/site_tasarimi.html` bu hâliyle güncellendi).

Girdi Excel dosyaları (derslik dosyası, gözetmen atamaları) bu depoda YOKTUR; her dönem yeniden verilir.

## Önemli kurallar
- Okul dosyasındaki sınavlar (3./4./11. kat: İktisada Giriş I, Sosyal Bilimler için Matematik I, Sosyolojide Temel Kavramlar, YBS laboratuvarları) `5_yerlestir.py` içindeki `EKSTRA` listesindedir; her kontrole girmelidir.
- 90 dakikalık ve 2 saatlik sınavlar (örn. İstatistik, Sosyal Bilimler için Matematik I) iki saat derslik ve gözetmen tutar, gözetmen yükünde 2 görev sayılır (`SURE_DK`).
- Gözetmen yalnızca "2+ derslikli sınavlar" listesindeki sınavlara atanır; sayıları listeyi hazırlayan belirler.
- Modeldeki yarıyıl etiketi gerçek öğrenci sınıfı değildir; çakışma ve öneri için gerçek ortak öğrencilere bakılır.
- Ana sayfadaki "Son değişiklikler" kutusu `Yöntem/degisiklikler.json` dosyasından gelir. Her sınav veya gözetmen değişikliğinde en üste bir satır eklenir.
- Panel şifresi `Yöntem/panel_sifre.txt` dosyasındadır (yüklenmez). Boşluk ve harf büyüklüğü fark etmez.
- Yüklemeden önce depo güncellenmeli (`git pull`); başkası dosyayı değiştirmiş olabilir.
- Tarayıcılar eski sayfayı önbellekte tutar; kontrol için adrese `?v=N` ekleyin.
