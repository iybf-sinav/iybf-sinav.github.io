# Sınav Takip Uygulaması

Adres: https://iybf-sinav.github.io/sinavtakipuygulamasi/ (eski `/bossablon/` adresi buraya yönlenir).

Bu klasör uygulamanın **kaynağıdır** ve aynı zamanda **demosudur**. Bütün geliştirme doğrudan buradaki
`index.html` üzerinde yapılır (v2'den türetme bitti; `2627vizeprogrami/v2/` bağımsız bir deneme olarak kalır).

## Dosyalar

- `index.html`: uygulamanın tamamı (Sınav Takip ve Sınav Zarfı Takip). Kod klasör adına bağlı değildir:
  düzenlemeler sayfanın bulunduğu klasörün `veri.json`, `epostalar.json`, `kurallar.json` dosyalarına yazılır.
- `veri.json`: boş veri. `meta.mode` = `"demo"` bu klasörü demo yapar (aşağıda). Biçim: kökteki `VERI-BICIMI.md`.
- `epostalar.json`: boş e-posta listesi.
- `kurallar.json`: genel kurallar (`"kapsam": "genel"`); yeni uygulamalara bunlar kopyalanır.

## Demo modu (`meta.mode: "demo"`)

- Sayfanın üstünde turuncu DEMO şeridi ve “Demo verisini sıfırla”, “Örnek veriyle doldur” düğmeleri vardır.
- Herkes girişsiz bütün düzenleme denetimlerini kullanır. Kayıtlar GitHub'a gitmez, yalnız o tarayıcıda saklanır
  (localStorage, anahtar `sinav-takip-demo:<klasör>`). Tarayıcı depolamaya izin vermezse kayıtlar yalnız bellekte
  tutulur ve şeritte uyarı çıkar.
- Kayıt katmanı tek yerdedir: `loadDoc` / `saveDoc` (demoda tarayıcı, gerçek dönemde GitHub Contents API).
  Sınav, duyuru, gözetmen/izin, bölüm, e-posta, program bilgisi, kural ve zarf kayıtlarının hepsi bu yoldan geçer.

## Yeni dönem: “Uygulama Oluştur”

Demonun en altındaki **Uygulama Oluştur** düğmesi, düzenleyici girişi (depoya yazma yetkisi olan GitHub anahtarı)
ile yeni bir klasör açar. Sorulanlar: üniversite, fakülte, sınav dönemi adı, sınav tarihleri ve adres uzantısı
(dönem adından önerilir, ör. “2026-2027 Güz Dönemi Final” → `2627guzfinal`; yalnız `a-z 0-9 -`; var olan
klasörlerle ve ayrılmış adlarla çakışamaz).

Oluşan klasör (tek commit, Git Data API; olmazsa dosya dosya Contents API):
- `index.html`: depodaki `sinavtakipuygulamasi/index.html` aynen,
- `veri.json`: boş veri + `meta` (`university`, `faculty`, `programName`, `period`; `mode` yok → gerçek dönem),
- `epostalar.json`: boş, `kurallar.json`: yalnız genel kurallar.

Yeni dönemde demo şeridi yoktur; düzenleme yalnız düzenleyici girişliyken açıktır ve klasörün kendi dosyalarına commit edilir.

## Dönemi silme

Gerçek bir dönemde, düzenleyici girişliyken Panel → Veriler'in en altında kırmızı **Bu dönemi sil** düğmesi vardır.
Onay için klasör adı yazılır; klasördeki bütün dosyalar tek commit'le silinir. Korumalı klasörlerde
(`sinavtakipuygulamasi`, `2627vizeprogrami` ve altı, `panel`, `kod`, kök vb.) ve demoda bu düğme hiç görünmez.

## Uygulama güncellenince

Mevcut dönemlerin `index.html`'i kendiliğinden güncellenmez (oluşturulduğu andaki kopyadır). Bir döneme yeni sürümü
almak için o klasörün `index.html`'ini buradakiyle değiştirmek yeterlidir; veri dosyalarına dokunulmaz.
Kökteki `index.html` yönlendirmesini başka bir döneme çevirmek ayrı bir karardır.
