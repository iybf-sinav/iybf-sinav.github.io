# Sınav Takip Uygulaması

Adres: https://iybf-sinav.github.io/sinavtakipuygulamasi/ (eski `/bossablon/` adresi buraya yönlenir).

Bu klasör uygulamanın **kaynağıdır** ve aynı zamanda **demosudur**. Bütün geliştirme doğrudan buradaki
`index.html` üzerinde yapılır (v2'den türetme bitti; `2627vizeprogrami/v2/` bağımsız bir deneme olarak kalır).

## Dosyalar

- `index.html`: uygulamanın tamamı (Sınav Takip ve Sınav Zarfı Takip). Kod klasör adına bağlı değildir:
  düzenlemeler sayfanın bulunduğu klasörün `veri.json`, `epostalar.json`, `kurallar.json` dosyalarına yazılır.
- `veri.json`: boş veri. `meta.mode` = `"demo"` bu klasörü demo yapar (aşağıda). Biçim: bu klasördeki `VERI-BICIMI.md`.
- `epostalar.json`: boş e-posta listesi.
- `kurallar.json`: genel kurallar (`"kapsam": "genel"`); yeni uygulamalara bunlar kopyalanır.
- `VERI-BICIMI.md`: `veri.json`'un tam biçimi (2. aşama alanları, uyarı kuralları ve Excel sayfa/sütun eşlemesi dahil).
- `YZ-REHBERI.md`: bir yapay zekâ oturumunun bu verisi nasıl okuyup yazacağı (kişisel öğrenci verisi yazılmaz).

## Kayıtlar, uyarılar, Ayarlar ve Kontrol (2. aşama)

- **Öğretim Üyeleri** sekmesi (düzenleyici): “+ Öğretim elemanı ekle”, düzenle/sil: ad, unvan, bölüm, e-posta, izinli gün/saatler
  (`teacherList`). Sınavı olan öğretim elemanı silinemez.
- **Gözetmenler** sekmesi: gözetmen ekle, izinli gün/saat (gün ya da tarih) ve e-posta (`proctorAvailability`).
- **Derslikler** sekmesi: “+ Derslik ekle”, düzenle/sil: kod, kat, sınav kapasitesi, tam kapasite (`rooms`). Kartlar kat kat;
  liste kayıtlar + sınavlardaki dersliklerin birleşimi. Sınav yapılan derslik silinemez.
- **Bölümler** (Sınav Programları): bölüm formunda “Sınıflar” (ör. 1, 2, 3, 4) → bölüm-sınıf etiketleri YBS1, İŞL1 …
- **Sınav formu**: tarih seçici, öğretim elemanı ve derslik listeden (yoksa “+ Yeni ekle” / “+ Listeye yeni derslik”),
  bölüm-sınıf çoklu seçim, kapasite derslik yanında, gözetmen “Seç” penceresi.
- **Uyarılar** (alan değiştikçe ve kaydetmeden önce): bölüm-sınıf, öğretim elemanı (çakışma, izin), derslik çakışması,
  kapasite esnemesi, gözetmen eşiği, art arda sınav → uyarı (“Yine de kaydet”); tam kapasite aşımı ve gözetmen
  çakışması/izni/kendi dersi → engel. `settings.warnOnly` kapalıysa uyarılar da kaydı durdurur.
- **Panel → Ayarlar**: gözetmen eşiği, kapasite esnemesi, art arda sınav sınırı, uzun sınav süresi (görev sayımı), yalnız uyar.
- **Panel → Kontrol**: bütün program aynı kurallarla taranır; sorun listesi (tür, ders, gün-saat, açıklama), tıklayınca sınav kartı.
- Bütün bu kayıtlar `veri.json`'a `loadDoc`/`saveDoc` yoluyla yazılır (demoda tarayıcıya, gerçek dönemde GitHub'a).

## Veri Tablosu, Excel ve yazdırma (3. aşama)

- **Panel → Veri Tablosu** (yalnız düzenleme yetkisi olanlara; demoda herkese): Sınavlar, Derslikler, Öğretim Elemanları,
  Gözetmenler, Bölümler, Duyurular sayfaları Excel gibi düzenlenir (hücreye yaz, Enter/Tab/oklarla gez, satır ekle/sil,
  başlığa basınca sırala, ara). Değişiklikler taslakta durur; **Değişiklikleri kaydet** taslağı tam doğrular (hatalı hücreler
  kırmızı, listeden hücreye gidilir), Kontrol kurallarını çalıştırır (`warnOnly`'e uyarak) ve `saveDoc` ile **tek kayıt** yapar. **Vazgeç** taslağı atar.
- Aynı sekmede **Verileri indir (Excel)**, **Şablon indir** (başlıklar + örnek satır) ve **Verileri yükle (Excel)**. Yükleme:
  doğrulama → önizleme (sayfa başına satır, hatalar, uyarılar) → kırmızı uyarı ve onay → tek kayıt. Hatalı dosyada kayıt yapılmaz.
  Sayfa/sütun düzeni: `VERI-BICIMI.md` → “Excel sayfa/sütun eşlemesi”. Panel → Veriler'deki eski düğme aynı dosyayı indirir.
- **Yazdır / PDF**: kişi, bölüm, derslik ve tüm program pencerelerinde; o anki liste ya da takvim (takvim A4 yatay) başlıklı bir
  yazdırma sayfası olarak açılır; tarayıcının “PDF olarak kaydet” seçeneğiyle PDF olur. Gözetmenler sekmesinde
  **Gözetmen görev çizelgesi**: her gözetmen ayrı sayfada (gün, saat, ders, derslik, toplam görev).
- Demoda “Örnek veriyle doldur” ile hepsi denenebilir.

## Demo modu (`meta.mode: "demo"`)

- Sayfanın üstünde turuncu DEMO şeridi ve “Demo verisini sıfırla”, “Örnek veriyle doldur” düğmeleri vardır.
- Herkes girişsiz bütün düzenleme denetimlerini kullanır. Kayıtlar GitHub'a gitmez, yalnız o tarayıcıda saklanır
  (localStorage, anahtar `sinav-takip-demo:<klasör>`). Tarayıcı depolamaya izin vermezse kayıtlar yalnız bellekte
  tutulur ve şeritte uyarı çıkar.
- Kayıt katmanı tek yerdedir: `loadDoc` / `saveDoc` (demoda tarayıcı, gerçek dönemde GitHub Contents API).
  Sınav, duyuru, gözetmen/izin, bölüm, e-posta, program bilgisi, kural ve zarf kayıtlarının hepsi bu yoldan geçer.

## Görünüm ve düzenleyici girişi (footer)

**Düzenleyici girişi** düğmesi footer'dadır (girişliyken “Düzenleyici: <kullanıcı> · Çıkış”). Düzenleme yetkisi olana
(demoda herkese, gerçek dönemde girişliyken) footer'da **Normal görünüm | Düzenleyici görünümü** seçicisi çıkar.
Normal görünüm ziyaretçinin gördüğü sayfadır (hiçbir düzenleme denetimi yok); seçim tarayıcıda hatırlanır, girişten
hemen sonra Düzenleyici görünümü açılır, çıkışta normal görünüme dönülür. Kodda tek denetim `editor` değişkenidir
(yetki && düzenleyici görünümü; `setEditor`).

## Yeni dönem: “Kendi uygulamanı oluştur”

Demoda sağ altta sabit duran **Kendi uygulamanı oluştur** düğmesi bir pencere açar: kısa açıklama (yeni adres, boş
program, verinin GitHub'da tutulması, düzenleyici girişi, silme) ve oluşturma formu; girişsizken giriş düğmesi.
Oluşturulan dönemlerde bu düğme yoktur. Oluşturma düzenleyici girişi (depoya yazma yetkisi olan GitHub anahtarı)
ile yeni bir klasör açar. Sorulanlar: üniversite, fakülte, sınav dönemi adı, sınav tarihleri ve adres uzantısı
(dönem adından önerilir, ör. “2026-2027 Güz Dönemi Final” → `2627guzfinal`; yalnız `a-z 0-9 -`; var olan
klasörlerle ve ayrılmış adlarla çakışamaz).

Oluşan klasör (tek commit, Git Data API; olmazsa dosya dosya Contents API):
- `index.html`: depodaki `sinavtakipuygulamasi/index.html` aynen,
- `veri.json`: boş veri + `meta` (`university`, `faculty`, `programName`, `period`; `mode` yok → gerçek dönem; boş `teacherList`, `rooms` ve varsayılan `settings`),
- `epostalar.json`: boş, `kurallar.json`: yalnız genel kurallar,
- `VERI-BICIMI.md` ve `YZ-REHBERI.md`: buradakiler aynen.

Yeni dönemde demo şeridi yoktur; düzenleme yalnız düzenleyici girişliyken açıktır ve klasörün kendi dosyalarına commit edilir.

## Dönemi silme

Gerçek bir dönemde, düzenleyici girişliyken Panel → Veriler'in en altında kırmızı **Bu dönemi sil** düğmesi vardır.
Onay için klasör adı yazılır; klasördeki bütün dosyalar tek commit'le silinir. Korumalı klasörlerde
(`sinavtakipuygulamasi`, `2627vizeprogrami` ve altı, `panel`, `kod`, kök vb.) ve demoda bu düğme hiç görünmez.

## Uygulama güncellenince

Mevcut dönemlerin `index.html`'i kendiliğinden güncellenmez (oluşturulduğu andaki kopyadır). Bir döneme yeni sürümü
almak için o klasörün `index.html`'ini buradakiyle değiştirmek yeterlidir; veri dosyalarına dokunulmaz.
Kökteki `index.html` yönlendirmesini başka bir döneme çevirmek ayrı bir karardır.
