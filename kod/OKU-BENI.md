# İYBF Sınav Programı: kodlar ve notlar

Bu klasör sayfayı üreten kodların güncel kopyasıdır (2 Kasım 2026). Canlı sayfa bu klasörün dışındaki `index.html` ve `panel/index.html` dosyalarıdır.

## Sayfa nasıl üretilir
1. `Yöntem/kod/7_gozetmenlik_formati.py` gözetmen kişi dosyalarını yazar.
2. `Yöntem/kod/9_panel_uret.py` şifreli panel sayfasını üretir (`panel/index.html` olarak yüklenir).
3. `Yöntem/kod/8_site_uret.py` ana sayfayı üretir (`index.html` olarak yüklenir).
4. Üretilen iki dosya bu deponun kökündeki `index.html` ve `panel/index.html` yerine konur ve yüklenir.

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
