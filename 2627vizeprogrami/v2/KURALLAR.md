# İYBF Sınav Programı ve Gözetmen Yerleştirme: Kurallar ve Kısıtlar

İstanbul Esenyurt Üniversitesi, İşletme ve Yönetim Bilimleri Fakültesi. Derleme tarihi: 4 Kasım 2026 (Kasım 2026 vize programından sonra, final öncesi).

Bu belge sınav yerleştirme kodunda, şablonda, devir notlarında, Excel çıktılarında ve sitede yazılı olan kuralları bir araya getirir. Kaynaklarda olmayan kural eklenmedi; açık olmayan yerler "belirsiz" diye işaretlendi.

## Nasıl okunur

- **Genel kural (her dönem)**: kodda ya da şablonda her dönem için yazılı kural.
- **Bu döneme özel karar**: Kasım 2026 vizesi için alınan karar. Finalde yeniden sorulmalı.
- Tür: **Sert** (kesinlikle uyulur), **Yumuşak** (mümkün olduğunca), **Sayım** (görev sayma kuralı), **Bilgi** (yöntem, not, veri).
- Kaynak: `dosya:satır` ya da `Excel dosyası / sayfa`. Yollar depo köküne göredir (`kod/...`).
- Bölüm 2-6'da "şablon" diye geçen kurallar Bahar 2025-26 yöntemindendir (`Yeni Dönem Şablonu.xlsx`, `2_programi_kur.py`). Kasım 2026'da çalışan kod `5_yerlestir.py`'dir; ikisinin farkları Bölüm 11'dedir.

## Özet

| Bölüm | Kural sayısı |
|---|---|
| 1. Genel takvim ve sınav süreleri | 9 |
| 2. Sınav yerleştirme: sert kısıtlar | 15 |
| 3. Sınav yerleştirme: yumuşak kısıtlar, öncelikler ve puanlama | 11 |
| 4. Derslikler: kapasite, esneme, bölme, kat, laboratuvar | 18 |
| 5. Gözetmenler: kim gözetmen ister, atama ilkeleri, başka birimler | 17 |
| 6. Gözetmen görev sayımı | 6 |
| 7. Veri tuzakları ve özel durumlar | 17 |
| 8. Yayından sonra gelen değişiklikler | 5 |
| 9. Bu dönemin kişiye ve derse özel kararları (Kasım 2026 vize) | 27 |
| 10. Site ve panel kuralları | 11 |
| 11. Çelişkiler ve belirsizlikler | 20 |
| 12. Finalde sorulması gerekenler | 15 |
| **Toplam** | **171** |

## 1. Genel takvim ve sınav süreleri

- **T1. Sınav haftası** · Bu döneme özel karar · Bilgi  
  Kasım 2026 vizesi 2-6 Kasım 2026, Pazartesi-Cuma (5 gün).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:26-27; kod/Belgeler/Devir Notu.md:7_
- **T2. Oturum saatleri** · Genel kural (her dönem) · Sert  
  Her sınav saat başında başlar. Günde 9 oturum vardır: 09:00, 10:00, …, 17:00. Standart sınav 50 dakika sürer (ör. 09:00-09:50).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:28; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 3; kod/Yöntem/Kod Anahtari.txt (son bölüm)_
- **T3. Çarşamba 09:00-12:00 yasak** · Bu döneme özel karar · Sert  
  Çarşamba 09:00, 10:00 ve 11:00 oturumlarına sınav konmaz. Kodda dönem ayarı olarak duruyor; her dönem geçerli olup olmadığı yazılı değil (belirsiz).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:29, 106-108; kod/Belgeler/Devir Notu.md:7; kod/Belgeler/Aşama 4 Seçenekleri.md:3_
- **T4. Süre yuvarlama** · Genel kural (her dönem) · Sert  
  Hocanın 60 dakikaya kadar yazdığı süre 50 dakika sayılır. 90 dakika gibi daha uzun süreler aynen uygulanır. Formda seçenekler '50 dk' ve '90 dk'dır.  
  _Kaynak: kod/Yöntem/kod/1_dersleri_yukle.py:30, 33, 559-563; kod/Yöntem/kod/0_hoca_formu.py:31; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 4_
- **T5. Uzun sınav iki oturum kapatır** · Genel kural (her dönem) · Sert  
  50 dakikadan uzun sınav (90 dk, 120 dk) dersliği ve öğrencileri iki oturum boyunca tutar. Bu yüzden 17:00'de 90 dakikalık sınav başlatılamaz (18:00'i geçer).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:495-496, 516-517; kod/Yöntem/kod/2_programi_kur.py:352-355; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 4_
- **T6. 120 dakikalık sınavlar** · Bu döneme özel karar · Bilgi  
  Derslik dosyasında tek saatlik hücre olarak yazılan ama uzun süren sınavlar kodda ayrıca tanımlanır: İstatistik 120 dk (Cuma 12:00-14:00), Sosyal Bilimler için Matematik I 120 dk (Cuma 16:00-18:00).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:1370, 1384-1385; kod/Belgeler/Devir Notu.md:146-147, 175-176_
- **T7. Formda boş bırakılan alanlar** · Genel kural (her dönem) · Bilgi  
  Hoca bilgi formunda boş bırakılan alanlar şöyle kabul edilir: yazılı sınav var / ders saatinde olması şart değil / 50 dk / izin günü yok.  
  _Kaynak: kod/Belgeler/2026-2027 Güz Vize - Hoca Bilgi Formu (Toplu) (1).xlsx / Yönerge_
- **T8. Okulun yaptığı ortak dersler** · Genel kural (her dönem) · Bilgi  
  Türk Dili, Yabancı Dil, Atatürk İlkeleri ve İnkılap Tarihi (Türkçe) sınavlarını Ortak Dersler Bölümü yapar; fakülte programına girmez. Şablona göre İngilizce karşılıkları programa girer.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 28; kod/Yöntem/kod/5_yerlestir.py:49-50, 804-805; kod/Belgeler/Devir Notu.md:47_
- **T9. Sınavı olmayan dersler** · Genel kural (her dönem) · Bilgi  
  Hocanın 'ödev/proje ile ölçülüyor' ya da 'sınav yapılmayacak' dediği dersler (ör. bu dönem 10 ders, Consumer Behaviour, Brand Management, Tourism Economics) programa girmez.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:78, 306, 331; kod/Yöntem/kod/0_hoca_formu.py:29; kod/Belgeler/Devir Notu.md:10, 100_

## 2. Sınav yerleştirme: sert kısıtlar

- **S1. Öğrenci çakışması (ortak öğrenci)** · Genel kural (her dönem) · Sert  
  Ortak öğrencisi olan iki dersin sınavı aynı oturumda olamaz. Ortak öğrenci OBS ders kayıtlarından bulunur; alttan, devamlı alttan, üstten ve yükseltme ile alanlar da sayılır. Aynı dersin farklı kodları çakışma sayılmaz.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:367-370; kod/Yöntem/kod/0b_cakisma_ciftleri.py:4-6, 51-57; kod/Belgeler/Devir Notu.md:37_
- **S2. Aynı bölüm-yarıyıl** · Genel kural (her dönem) · Sert  
  Ders programında (PDF) aynı bölüm-yarıyıl grubunda olan iki sınav aynı anda olamaz.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:372-373; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 16; kod/Yöntem/REHBER.md:75_
- **S3. Aynı öğretim elemanı** · Genel kural (her dönem) · Sert  
  Bir hocanın iki sınavı aynı anda olamaz. İstisna: hocanın aynı derslikte birlikte yapmak istediği sınavlar (birleşik sınavlar) ve bu dönem Meysure Evren Çelik Sütiçer'in muaf dersleri (bkz. K1).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:371, 374-375; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 17_
- **S4. ÇAP çiftleri (çapraz)** · Genel kural (her dönem) · Sert  
  ÇAP öğrencilerinin kimliği bilinmediği için şu çiftlerde iki bölümün dersleri birbiriyle aynı oturuma konmaz: Havacılık ↔ Lojistik, E-Ticaret ↔ Havacılık. Yalnız iki bölümün dersleri birbiriyle karşılaştırılır (bir bölümün kendi dersleri değil).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:87-89, 357-364, 376-378; kod/Belgeler/Devir Notu.md:37, 133_
- **S5. Çakışma grubunun belirlenmesi** · Genel kural (her dönem) · Sert  
  Çakışma grubu = programdaki bölüm-yarıyıl + hocanın 'dersi alan bölümler' bilgisi + sistemde dersi alan görünen her bölüm. Şüphede grup eklenir. Güz kodunda bir bölümün 'dersi alıyor' sayılması için OBS'te en az 3 öğrencisi olmalı.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 19; kod/Yöntem/kod/1_dersleri_yukle.py:36-37; kod/Yöntem/kod/5_yerlestir.py:332-333; kod/Yöntem/REHBER.md:76-77_
- **S6. Çok programlı ders tek sınavdır** · Genel kural (her dönem) · Sert  
  Birden çok programa verilen ders tek sınavdır ve aldığı bütün gruplarla çakışmamalıdır.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 18_
- **S7. Fakülte seçmeli havuzu** · Genel kural (her dönem) · Sert  
  Havuz dersleri ayrıca HAVUZ grubu alır; aynı havuzdaki seçmeliler farklı saatlere konur. (Bahar şablonu kuralı; Güz kodunda ayrı bir havuz kontrolü görülmedi.)  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 20; kod/Yöntem/Kod Anahtari.txt (ÖZEL KODLAR)_
- **S8. Ardışık sınav sınırı (öğrenci bazında)** · Bu döneme özel karar · Sert  
  Kasım 2026 kuralı (20 Ekim): hiçbir öğrenci aynı gün 3 ardışık oturumda sınava girmez. Alttan alanlar dahil. Bir sınav bu yüzden hiç yerleşemiyorsa kural o sınav için gevşetilir ve sınav 'gevşek' diye işaretlenir. Günde toplam sınav sayısına sınır yok.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:493, 498-511, 523-524, 716-727; kod/Belgeler/Devir Notu.md:42, 56, 127_
- **S9. Ardışık sınav sınırı (şablondaki eski kural)** · Genel kural (her dönem) · Sert  
  Şablondaki genel kural: bir program-yarıyıl grubunun kendi bölüm dersleri aynı gün en fazla 2 sınav arka arkaya olabilir; alttan alınan dersler dahil edilmez. Güz kodu bunu yalnız ceza olarak sayar (bkz. Y3), sert kural S8'dir.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 21; kod/Yöntem/kod/2_programi_kur.py:35, 366-374; kod/Yöntem/REHBER.md:78_
- **S10. Akademik izin günü** · Genel kural (her dönem) · Sert  
  Hocanın sınavı akademik izin gününe konmaz. Hoca bir dersinde izin günü yazdıysa bu gün bütün sınavlarına uygulanır. Formdaki yanlış girişler kodda düzeltilebilir (IZIN_DUZELT).  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 23; kod/Yöntem/kod/1_dersleri_yukle.py:702-720; kod/Yöntem/kod/5_yerlestir.py:39-40, 334-342, 521-522_
- **S11. Hoca dolu saatleri ve gün kısıtları** · Genel kural (her dönem) · Sert  
  Hocanın başka yerde dersi olduğu saatlere (HOCA_DOLU) ve derse özel gün kısıtlarına (GUN_KISITI) sınav konmaz.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:518-520, 528-531_
- **S12. İki büyük ders aynı oturumda olmaz** · Genel kural (her dönem) · Sert  
  100 ve üzeri öğrencili iki sınav aynı oturuma konmaz.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:37, 540-541_
- **S13. Tam kapasite aşılmaz** · Genel kural (her dönem) · Sert  
  Bir dersliğe tam (yan yana) kapasitesinden fazla öğrenci konmaz. Esneme hiçbir zaman tam kapasiteyi geçemez.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:31, 385, 457; kod/Belgeler/Devir Notu.md:39, 72_
- **S14. Sabit sınavlar** · Genel kural (her dönem) · Sert  
  SABIT listesindeki sınav önce, kendi gün/saatine konur; bu sınavda izin günü ve ardışık kuralı denetlenmez. Yerleşemezse program durur.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:521-524, 673-681_
- **S15. Bağımsız kontrol** · Genel kural (her dönem) · Bilgi  
  Çakışma kontrolü kodun kendi sonucuna göre değil, çıktı dosyasından bağımsız yapılır (öğrenci, hoca, derslik, kapasite, Çarşamba 09-12, izin). Kullanıcının elle değiştirdiği dosya da aynı kontrolden geçer. Okul dosyasındaki sınavlar (EKSTRA) her kontrole girer.  
  _Kaynak: kod/Belgeler/Devir Notu.md:125, 168-169; kod/OKU-BENI.md:14_

## 3. Sınav yerleştirme: yumuşak kısıtlar, öncelikler ve puanlama

- **Y1. Yerleştirme sırası** · Genel kural (her dönem) · Yumuşak  
  Sınavlar şu sırayla yerleştirilir: (1) onaylı kilitli sınavlar (KILIT), (2) öncelikli hocaların sınavları (PRIORITY_HOCA), (3) 100+ öğrencili sınavlar, (4) en çok sınavla çakışanlar, (5) öğrencisi çok olanlar.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:683-687_
- **Y2. Kilitli (onaylı) sınavlar** · Genel kural (her dönem) · Yumuşak  
  Önceki aşamada onaylanan sınavlar KILIT sözlüğüyle sabitlenir; önce kilitli yerlerinde denenir, kurallar izin veriyorsa orada kalır.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:66-69, 697-704; kod/Belgeler/Devir Notu.md:34_
- **Y3. Oturum seçme puanı** · Genel kural (her dönem) · Yumuşak  
  Uygun oturumlar şu sırayla karşılaştırılır (önce gelen daha önemli): 1) hocanın 'ders günü ve saatinde' talebi karşılanıyor mu, 2) hocanın tercih saati, 3) aynı oturumdaki ÇAP yumuşak çiftleri, 4) bir bölüm-yarıyıl grubunun 3 ardışık sınavı, 5) esneme miktarı, 6) büyük derslerin aynı güne yığılması, 7) günün toplam sınav yükü, 8) 13:00'e uzaklık, 9) daha erken oturum.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:705-715_
- **Y4. Hoca gün/saat talebi** · Genel kural (her dönem) · Yumuşak  
  Hocanın 'sınav dersin gün ve saatinde yapılsın' talebi mümkün olduğunca karşılanır (yumuşak). Kasım 2026'da yaklaşık 69 talepten 53'ü karşılandı; karşılanamayanların nedeni (çoğu Çarşamba 09-12, ardışık kural ve çakışma) raporlanır.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:601, 630-638; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 25; kod/Belgeler/Devir Notu.md:40_
- **Y5. İzin günü bilinmeyen hoca** · Genel kural (her dönem) · Yumuşak  
  İzin günü bilinmiyorsa (çoğunlukla ders saati ücretli hocalar) sınav, dersin dönem içindeki normal gün ve saatine konmaya çalışılır.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 24; kod/Yöntem/kod/1_dersleri_yukle.py:38; kod/Yöntem/REHBER.md:82-83_
- **Y6. ÇAP yumuşak çiftleri** · Genel kural (her dönem) · Yumuşak  
  İşletme ↔ YBS ve Siyaset ↔ Havacılık dersleri mümkünse aynı oturuma konmaz. Kullanıcı kararı (21 Ekim): İngilizce SBUİ grubu ile Türkçe Havacılık dersi bu kurala girmez (kod henüz ayırmıyor).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:86, 604-611; kod/Belgeler/Devir Notu.md:37, 92_
- **Y7. Öncelikli hocalar** · Bu döneme özel karar · Yumuşak  
  PRIORITY_HOCA listesindeki hocaların sınavları kilitli sınavlardan hemen sonra, diğerlerinden önce yerleşir. Bu dönem: Dikran Zenginkuzucu.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:65, 684-686; kod/Belgeler/Devir Notu.md:44_
- **Y8. Bahar (v2) puan ağırlıkları** · Genel kural (her dönem) · Yumuşak  
  2_programi_kur.py (Bahar v2 yöntemi) puanla seçer: hocanın açık talebi gün+saat 60, yalnız gün 45, yalnız saat 15; izin günü bilinmeyen hocada ders saati 25 / ders günü 8; 60'tan kalabalık sınavın 3. kata gitmesi 90; 3.+6. kat karışık bölünme -10; her ek derslik -4; kapasite aşımı öğrenci başı -0,4; gün yükü -0,3; aynı grubun aynı gün ikinci sınavı -8.  
  _Kaynak: kod/Yöntem/kod/2_programi_kur.py:39-49, 358-397_
- **Y9. Kesin talep (tarihli ya da özel derslik)** · Genel kural (her dönem) · Sert  
  Hoca tarih yazarak talep ettiyse ya da Kütüphane Lab / 7. kat gibi özel derslik istediyse gün/saati kesin (sert) kabul edilir (Bahar v2 yöntemi).  
  _Kaynak: kod/Yöntem/kod/2_programi_kur.py:128-129; kod/Yöntem/kod/donem_ayarlari_ornek.py:41_
- **Y10. Önce derslik müsaitliği sorulur** · Genel kural (her dönem) · Bilgi  
  Program kurulmadan önce derslik müsaitliği mutlaka sorulur; başka fakülteler de aynı derslikleri kullanır.  
  _Kaynak: kod/Yöntem/REHBER.md:52; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 6_
- **Y11. Sabah 09:00** · Bu döneme özel karar · Yumuşak  
  Kullanıcı birçok dersi bilerek 09:00'dan çekti; önerilerde 09:00 oturumları ayrı gösterilmeli.  
  _Kaynak: kod/Belgeler/Devir Notu.md:129_

## 4. Derslikler: kapasite, esneme, bölme, kat, laboratuvar

- **D1. 6. kat sınav kapasiteleri** · Bu döneme özel karar · Sert  
  6A1: 35, 6A2: 33, 6D1: 17, 6D3: 23, 6D4: 25, 6D5: 23 (toplam 156).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:30; kod/Belgeler/Devir Notu.md:39; Aşama 2 - Derslik Dosyası (6. Kat) başlığı_
- **D2. 6. kat tam kapasiteleri (kesin üst sınır)** · Genel kural (her dönem) · Sert  
  6A1: 50, 6A2: 47, 6D1: 29, 6D3: 32, 6D4: 40, 6D5: 37. Hiçbir durumda aşılmaz.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:31; kod/Belgeler/Devir Notu.md:39_
- **D3. 3. ve 4. kat salon sınav kapasiteleri** · Bu döneme özel karar · Bilgi  
  Kullanıcının verdiği değerler: 3A1: 90, 3A3: 85, 3A5: 60, 3A6: 50, 4A3: 80, 4A4: 50. Okul dosyası başlığındaki sayı tam kapasitedir.  
  _Kaynak: kod/Yöntem/kod/8_site_uret.py:55-56; kod/Belgeler/Devir Notu.md:103_
- **D4. Esneme** · Bu döneme özel karar · Yumuşak  
  Sınav kapasitesi şu kadar aşılabilir (tam kapasiteyi geçmeden): normal +5; bir dersin gruplarını daha az dersliğe toplamak için +8'e kadar (kullanıcı onayı 20 Ekim); 100+ öğrencili derslerde +20'ye kadar. Esneme son çaredir: önce esnemesiz (gerekirse bölerek) denenir.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:34-37, 461-463; kod/Belgeler/Devir Notu.md:39, 72, 77_
- **D5. Derslik seçiminde sıra** · Genel kural (her dönem) · Yumuşak  
  Bir sınav için derslik takımı seçilirken önce bölünen bölüm sayısı en az olan (İşletme'nin bölünmesi sayılmaz), sonra toplam bölünme en az, sonra derslik sayısı en az, sonra esneme en az olan seçilir.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:461-483; kod/Belgeler/Devir Notu.md:72_
- **D6. Bölüm tek derslikte** · Genel kural (her dönem) · Sert  
  Her bölüm mümkünse tek derslikte sınava girer. Sığmazsa EŞİT parçalara bölünür (2-3 kişilik artık parça olmaz); her parça en az 8 kişi. Önce bir bölüm en çok 2 dersliğe bölünür, olmazsa daha fazla. Gerekirse tercihen İşletme bölünür.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:38, 399-404, 464, 477; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 12; kod/Belgeler/Devir Notu.md:39_
- **D7. Bölünen bölümde kim nereye** · Genel kural (her dönem) · Sert  
  Bölünen bir bölümün öğrencileri öğrenci numarası sırasına göre ardışık bloklara ayrılır (numara = giriş yılı sırası: eski girişliler bir derslikte, yeniler diğerinde). Sayı farkı kalırsa son parçaya eklenir. Bu liste öğrenci no içerir, paylaşılmaz.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:774-780, 1190-1194; kod/Belgeler/Devir Notu.md:39_
- **D8. Aynı kodlu dersi farklı hocalar veriyorsa** · Bu döneme özel karar · Sert  
  Aynı kodlu dersi farklı hocaların verdiği öğrenci grupları aynı dersliğe karıştırılmaz (AYRI; bu dönem 20G1010).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:52-54, 388-390_
- **D9. Bir derslikte bir sınav** · Genel kural (her dönem) · Sert  
  Bir derslikte aynı saatte tek sınav yapılır; birlikte yapılması onaylanan sınavlar hariç. Kapasite yetmezse sınav birden fazla dersliğe bölünür.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 7; kod/Yöntem/kod/5_yerlestir.py:542-543_
- **D10. Kat önceliği: önce 6. kat** · Bu döneme özel karar · Sert  
  Önce 6. kat derslikleri doldurulur. Kasım 2026 kararı: 3. kata kullanıcı onayı olmadan sınav yerleştirilmez (kod yalnız 6. kat dersliklerini dağıtır; 3./4./11. kat sınavları okul dosyasından elle gelir).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:30, 532; kod/Belgeler/Devir Notu.md:39; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 9_
- **D11. 60'tan kalabalık sınav 3. kata (şablon kuralı)** · Genel kural (her dönem) · Yumuşak  
  Şablondaki genel kural: 60'tan fazla öğrencili sınav 3. kata yazılır ve bu, hocanın gün/saat talebinden önce gelir. 3. kat yetmezse en büyük kısım 3. kata, kalanı 6. kata. Bölünen sınavda derslikler mümkünse aynı katta. Güz kodu bunu uygulamadı (bkz. D10, C4).  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 10-11; kod/Yöntem/kod/2_programi_kur.py:32, 44-46; kod/Yöntem/REHBER.md:80_
- **D12. Hocanın gireceği 25-29 kişilik sınav** · Genel kural (her dönem) · Sert  
  Şablon kuralı: 30'un altındaki sınav bölünmez (hoca iki derslikte olamaz); 25-29 öğrencili sınavlar 6D4 ya da 6D5'e tek derslik olarak yazılır.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 8; kod/Yöntem/kod/2_programi_kur.py:34_
- **D13. Az derslik** · Genel kural (her dönem) · Yumuşak  
  Çok bölümlü ya da kalabalık sınavlar mümkünse 2-3 dersliğe toplanır; her ek derslik ek gözetmen demektir.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 13; kod/Yöntem/kod/2_programi_kur.py:47_
- **D14. Derslik müsaitliği** · Genel kural (her dönem) · Sert  
  Derslikler yalnız boş olduğu bildirilen gün/saatlerde kullanılır. Kasım 2026'da 3./4. kat salonları için okulun gönderdiği dosya esas alındı (VİZE Derslik Dosyası 22.10.2026).  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 6; kod/Belgeler/Devir Notu.md:103_
- **D15. Laboratuvar** · Genel kural (her dönem) · Sert  
  Hoca laboratuvar isterse sınav yalnız laboratuvarda yapılır; laboratuvarda aynı saatte tek sınav. Kodda tek 'LAB' (40 kişi varsayımı) var; gerçek lab adları ve kapasiteleri kullanıcıdan istenecek. Kasım 2026'da 5 lab sınavını (Ülker Başar) kullanıcı kendisi yerleştirdi (4L1, 11L8, 4D8, 11L5; 90 dk).  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 14; kod/Yöntem/kod/5_yerlestir.py:32-33, 305, 532, 1375-1380; kod/Belgeler/Devir Notu.md:43, 105_
- **D16. Okul dosyasındaki sınavlar (EKSTRA)** · Bu döneme özel karar · Bilgi  
  3./4./11. kat ve lab sınavları 6. kat derslik dosyasında yoktur; kodda EKSTRA listesindedir ve bölüm programına, çakışma kontrolüne ve siteye bu listeden girer.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:1365-1404; kod/OKU-BENI.md:14; kod/Belgeler/Devir Notu.md:168_
- **D17. Kullanıcının derslik dosyası esastır** · Genel kural (her dönem) · Bilgi  
  Kullanıcının elle düzenlediği Derslik Dosyası (6. Kat) programın gerçeği kabul edilir; kod onu ezmez, kendi çıktısını '(kod çıktısı)' adıyla ayrı yazar. Sayısı yazılmayan derslikler eşit bölünür; birleşik toplam yazılmışsa listedeki sayı esas alınır.  
  _Kaynak: kod/Belgeler/Devir Notu.md:71, 84, 97, 107; kod/Yöntem/kod/5_yerlestir.py:1407-1538_
- **D18. Sınırda yerleşim istenmiyor** · Bu döneme özel karar · Yumuşak  
  Kullanıcı tam kapasite sınırında yerleşim istemiyor (ör. 28 kişi, tam kapasite 29).  
  _Kaynak: kod/Belgeler/Devir Notu.md:77_

## 5. Gözetmenler: kim gözetmen ister, atama ilkeleri, başka birimler

- **G1. Gözetmen eşiği** · Genel kural (her dönem) · Sert  
  Sınavın öğrenci sayısı 30 ve üzeriyse gözetmen yazılır; 30'un altındaysa sınava dersin hocası girer. Birlikte yapılan sınavlarda toplam öğrenciye bakılır. (Kasım 2026 uygulaması farklı, bkz. G4 ve C5.)  
  _Kaynak: kod/Yöntem/kod/1_dersleri_yukle.py:34, 566-586; kod/Yöntem/kod/0_hoca_formu.py:42-43; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 30; kod/Belgeler/2026-2027 Güz Vize - Hoca Bilgi Formu (Toplu) (1).xlsx / Yönerge_
- **G2. Hoca gözetmen istedi ama öğrenci 30'un altında** · Genel kural (her dönem) · Bilgi  
  Karar kullanıcıya sorulur; onaylanan dersler listeye yazılır.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 31; kod/Yöntem/kod/1_dersleri_yukle.py:574-579; kod/Yöntem/kod/donem_ayarlari_ornek.py:37_
- **G3. Derslik başına gözetmen** · Genel kural (her dönem) · Sert  
  Gözetmen gereken sınav birden çok dersliğe bölünürse her dersliğe 1 gözetmen yazılır. 3. kat dersliklerinde 2 gözetmen (kalabalık salon). 4. kat salonları için de 2 varsayıldı.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 32-33; kod/Yöntem/kod/2_programi_kur.py:399-400; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx (alt not)_
- **G4. Kasım 2026 uygulaması: yalnız 2+ derslik listesi** · Bu döneme özel karar · Sert  
  Gözetmen yalnız kullanıcının hazırladığı '2+ Derslikli Sınavlar' listesindeki sınavlara atanır; sayıları listeyi hazırlayan belirler (M sütunu). Listede olmayan sınava gözetmen eklenmez. Kullanıcı sonradan tek tek ekleyebilir (ör. Dış Ticaret İşlemleri Muhasebesi, Maliyet Muhasebesi).  
  _Kaynak: kod/OKU-BENI.md:16; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Kontrol; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx_
- **G5. Çok derslikli sınavda bir dersliğe hoca girer** · Bu döneme özel karar · Bilgi  
  Kullanıcı bazı çok derslikli sınavlarda küçük dersliği hocaya bıraktı (ör. İşletmeye Giriş 6D5, Küresel Rekabetçilik 6D3, Bölgesel Çalışmalar 6A2, Havacılıkta Stratejik Yönetim 6D5, Gümrük Mevzuatı 6A2). Sitede o derslik 'Dersin hocası (gözetmen gerekmiyor)' görünür.  
  _Kaynak: kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx; veri.json; kod/Yöntem/kod/8_site_uret.py:228-229_
- **G6. İzin günü** · Genel kural (her dönem) · Sert  
  Gözetmene izin gününde görev yazılmaz.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 35; kod/Yöntem/kod/2_programi_kur.py:593-595; kod/Yöntem/izinler.json_
- **G7. Aynı saatte tek görev** · Genel kural (her dönem) · Sert  
  Bir gözetmen aynı saatte iki dersliğe ya da iki sınava yazılmaz; o saatte kendi dersinin sınavı varsa başka sınava yazılmaz. Uzun sınav kapsadığı bütün saatlerde kişiyi meşgul tutar.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 36; kod/Yöntem/kod/2_programi_kur.py:596-597; VERI-BICIMI.md:183-190_
- **G8. Kişisel saat kısıtları** · Genel kural (her dönem) · Sert  
  Gözetmenin kişisel saat kısıtlarına (ör. 'sabah 9, 10 olmasın') uyulur.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 37; kod/Yöntem/kod/2_programi_kur.py:84-86, 594_
- **G9. Üst üste 3 görev** · Genel kural (her dönem) · Sert  
  Şablon kuralı: bir gözetmene üst üste 3 sınav yazılmaz (muaf tutulanlar hariç). Kasım 2026'da Cuma 15:00-18:00 yığılması yüzünden (23 Ekim) sert olmaktan çıkarıldı, ceza ile en aza indirildi.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 38; kod/Yöntem/kod/2_programi_kur.py:37, 598-606; kod/Belgeler/Devir Notu.md:147_
- **G10. Kendi dersine giren gözetmen** · Genel kural (her dönem) · Sayım  
  Ders veren gözetmen kendi sınavına kendisi girer; bu görev gözetmenlik sayısına dahildir.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 39; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Gözetmen Yükü (başlık); kod/Belgeler/Devir Notu.md:112_
- **G11. Eşit toplam yük** · Genel kural (her dönem) · Yumuşak  
  Her gözetmene olabildiğince eşit sayıda görev yazılır (kendi sınavları dahil). Kod, en yüklüden en az yüklüye fark 1'e inene kadar görev taşır.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 40; kod/Yöntem/kod/2_programi_kur.py:608-611, 636-651_
- **G12. Eşit İngilizce sınav yükü** · Genel kural (her dönem) · Yumuşak  
  Her gözetmene olabildiğince eşit sayıda İngilizce sınav yazılır. İngilizce sınav = çakışma grubunda PSIR, BUS ya da ECF geçen sınav.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 41; kod/Yöntem/kod/2_programi_kur.py:108, 611, 653-670_
- **G13. İki gözetmenli derslikte kadın-erkek** · Genel kural (her dönem) · Yumuşak  
  İki gözetmenli derslikte (3./4. kat) mümkünse bir kadın bir erkek olur. Kasım 2026'da cinsiyet bilgisi gelmediği için uygulanmadı.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 42; kod/Yöntem/kod/2_programi_kur.py:617-619; kod/Belgeler/Devir Notu.md:112, 143_
- **G14. Az güne toplama / çok güne yayma** · Genel kural (her dönem) · Yumuşak  
  'Az güne toplansın' ya da 'çok güne yayılsın' tercihleri mümkün olduğunca uygulanır; bir görevin hemen öncesi/sonrası doluysa küçük ceza verilir. Kasım 2026: Melih Mert Oskay az güne toplandı.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 43; kod/Yöntem/kod/2_programi_kur.py:612-616; kod/Belgeler/Devir Notu.md:112_
- **G15. Atama sırası** · Genel kural (her dönem) · Yumuşak  
  Gözetmen atamasında önce en az uygun adayı olan görevler doldurulur; her görev için o an maliyeti en düşük kişi seçilir (yük ×10, İngilizce yük ×8, tercihler).  
  _Kaynak: kod/Yöntem/kod/2_programi_kur.py:608-634_
- **G16. Başka birimlere gözetmen** · Genel kural (her dönem) · Sayım  
  Sağlık Bilimleri Fakültesi (SBF) ve üniversite ortak seçmeli derslerine İYBF'den gözetmen verilebilir. Bunlar 'başka birim' kaydı olarak girer, 60 dakika sayılır, İYBF sınav sayısına girmez, gözetmen yüküne girer.  
  _Kaynak: kod/Yöntem/kod/8_site_uret.py:151-169; VERI-BICIMI.md:122-124; kod/Belgeler/Devir Notu.md:151, 172, 179_
- **G17. Yalnız isteneni değiştir** · Genel kural (her dönem) · Bilgi  
  Gözetmen atamasına sonradan gelen değişiklikte mevcut atamalara dokunulmaz; yalnız istenen satır değişir. İstenmeden yapılan yük dengelemesi geri alındı (30 Ekim).  
  _Kaynak: kod/Belgeler/Devir Notu.md:151, 198; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Kontrol (30 Ekim geri alma)_

## 6. Gözetmen görev sayımı

- **GS1. Uzun sınav 2 görev** · Genel kural (her dönem) · Sayım  
  Süresi 60 dakikadan uzun sınav (90 dk, 120 dk) gözetmen için 2 görev sayılır; 50-60 dk sınav 1 görev. (Kullanıcı kararı 22 Ekim; komisyon kuralı.)  
  _Kaynak: kod/Yöntem/kod/7_gozetmenlik_formati.py:40, 79; kod/Yöntem/site_tasarimi.html:2414-2419; kod/OKU-BENI.md:15; kod/Belgeler/Devir Notu.md:117_
- **GS2. Kendi dersi dahil** · Genel kural (her dönem) · Sayım  
  Toplam görev sayısına gözetmenin kendi dersindeki gözetmenliği dahildir.  
  _Kaynak: kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Gözetmen Yükü (başlık); kod/Yöntem/site_tasarimi.html:2421; kod/Yöntem/panel_sablonu.html:341_
- **GS3. Muafiyet sınavı** · Bu döneme özel karar · Sayım  
  Ortak dersler muafiyet sınavındaki görev saat olarak (2 saat) Toplam'a eklenir (3 Kasım). Liste 2'de 12 gözetmene 2, Seda Emir ve Şeyma Sertçelik'e 0 yazılı. Muafiyet sınavının tarihi/saati kaynaklarda yok (belirsiz).  
  _Kaynak: kod/Yöntem/panel_sablonu.html:333-341; kod/Yöntem/kod/9_panel_uret.py:96; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Gözetmen Yükü (sütun L); git 5e23da9, a35516e_
- **GS4. Başka birim görevleri** · Genel kural (her dönem) · Sayım  
  SBF ve ortak seçmeli görevleri 60 dakika kaydedilir, yani 1 görev sayılır.  
  _Kaynak: kod/Yöntem/kod/8_site_uret.py:161; kod/Yöntem/site_tasarimi.html:2416-2419_
- **GS5. Sitedeki sayım** · Genel kural (her dönem) · Sayım  
  Site gözetmen başına farklı sınavları sayar (aynı sınavda iki derslik tek sayılır), her sınavı süresine göre 1 ya da 2 ile çarpar. 'Gerekmiyor' görev değildir. Çok derslikli sınavda hocanın '(kendi sınavı)' kaydı siteye görev olarak girmez; tek derslikli sınavda '(dersin hocası)' olarak girer.  
  _Kaynak: kod/Yöntem/site_tasarimi.html:2421-2434; VERI-BICIMI.md:128; kod/Yöntem/kod/8_site_uret.py:135-144_
- **GS6. Paneldeki meşgul saat** · Genel kural (her dönem) · Sayım  
  Panel, bir görevin kaç saat tuttuğunu süreyi 60'a bölüp yukarı yuvarlayarak bulur (50 dk = 1 saat, 90 dk = 2, 120 dk = 2).  
  _Kaynak: kod/Yöntem/kod/9_panel_uret.py:97-103_

## 7. Veri tuzakları ve özel durumlar

- **V1. Ders Programı PDF'i esastır** · Genel kural (her dönem) · Bilgi  
  Hangi derslerin sınavı yapılacağını ve dersin hocasını Ders Programı PDF'i belirler. OBS yalnız öğrenci sayısı/listesi için kullanılır; OBS'te olup PDF'te olmayan dersler eklenmez, kontrol raporuna yazılır.  
  _Kaynak: kod/Yöntem/kod/kaynaklar.py:4-7; kod/Belgeler/Devir Notu.md:56, 67_
- **V2. OBS'te aynı dersin ikinci kodu** · Bu döneme özel karar · Bilgi  
  OBS'te bazı derslerin ikinci bir kodu var; bu öğrenciler de sınava eklenir (EK_OBS: Şehir ve Kültür, Finansal Yönetim, Örgütsel Davranış Araştırmaları, Havacılıkta Stratejik Yönetim, Depolama, İstatistik).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:148-151; kod/Belgeler/Devir Notu.md:64_
- **V3. Aynı kodu taşıyan farklı dersler** · Genel kural (her dönem) · Bilgi  
  PDF'te aynı kodu iki farklı ders taşıyabiliyor (Endüstri 4.0 / Liman ve Terminal; Organizational Behavior / Theory of International Trade; Regional Studies: Eurasia / History of Turkish Economy; Derivatives / Political Economics). Yalnız AYNI ADLI dersler birleştirilir.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:154-174, 238; kod/Belgeler/Devir Notu.md:65_
- **V4. Aynı ad, farklı hoca, farklı bölüm** · Bu döneme özel karar · Bilgi  
  Aynı adlı dersi farklı hocalar farklı bölümlere veriyorsa ayrı sınav yapılabilir (SPLIT_HOCA; şu an 2017G4021). Introduction to Economics-I 23 Ekim'de tek sınav yapıldı (hoca İlknur Şimşek).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:177-217; kod/Belgeler/Devir Notu.md:66, 138_
- **V5. İkinci hoca** · Bu döneme özel karar · Bilgi  
  İşletmeye Giriş (Şahin/Bakın) bilerek tek sınav. OBS'te BİT, Finansal Muhasebe I, İstatistik, Temel Hukuk, Hava Kargo için PDF'te olmayan ikinci hocalar var: tek sınav, hoca çakışması yalnız PDF hocasına göre.  
  _Kaynak: kod/Belgeler/Devir Notu.md:66_
- **V6. Birleşik (TR/İng) sınavlar** · Bu döneme özel karar · Bilgi  
  Hocanın istediği Türkçe/İngilizce karşılıklar aynı gün, saat ve derslikte tek sınav olur (BIRLESTIR: History of European Integration / Avrupa Bütünleşme Tarihi; International Law-I / Uluslararası Hukuk I). Diplomasi Tarihi I + Diplomatic History I ve Şehir ve Kültür + City and Culture da birlikte yapılıyor ama kodda tanımlı değil; kontrol sahte 'aynı hoca' uyarısı verir.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:61-63, 242-245; kod/Belgeler/Devir Notu.md:45, 129_
- **V7. Yarıyıl etiketi gerçek sınıf değil** · Genel kural (her dönem) · Bilgi  
  Modeldeki yarıyıl etiketi öğrencinin gerçek sınıfı değildir; çakışma ve öneri için gerçek ortak öğrencilere bakılır. Bölüm programındaki sınıf: kullanıcı düzeltmesi (SINIF_DUZELT) > OBS sınıfı.  
  _Kaynak: kod/OKU-BENI.md:17; kod/Yöntem/kod/6_bolum_programi.py:53-62, 99_
- **V8. Türkçe ve İngilizce programlar ayrı** · Genel kural (her dönem) · Bilgi  
  Bölüm/sınıf bazlı kontrolde Türkçe ve İngilizce programlar ayrı sayılır; birleştirilince sahte çakışma çıkıyor (18 sahte çift, gerçekte 3).  
  _Kaynak: kod/Belgeler/Devir Notu.md:125_
- **V9. Kontrolde sınavın kendi öğrenci listesi** · Genel kural (her dönem) · Bilgi  
  Kontrollerde öğrenci listesi olarak sınavın kendi listesi kullanılır; dersin bütün kodlarındaki öğrenciler değil (hocaya göre ayrılan sınavlarda yanlış uyarı verir).  
  _Kaynak: kod/Belgeler/Devir Notu.md:122_
- **V10. Ad eşleştirme** · Genel kural (her dönem) · Bilgi  
  Aynı hoca farklı yazılabilir (unvan, büyük/küçük harf); adlar tekilleştirilir. Ders adları tam eşlenir ('İstatistik' ≠ 'İstatistik ve Olasılık').  
  _Kaynak: kod/Yöntem/REHBER.md:111; kod/Belgeler/Devir Notu.md:126_
- **V11. Formun her sütunu kullanılır** · Genel kural (her dönem) · Bilgi  
  Hoca formundaki her sütun (sınav var, gün-saat, süre, gözetmen, izin, lab, aynı anda, eksik bölüm, ek öğrenci) programa yansımalı. Ek öğrenci tahminleri OBS sayısına eşit çıktığı için eklenmedi.  
  _Kaynak: kod/Belgeler/Devir Notu.md:124_
- **V12. Kayıtta görünmeyen dersler** · Bu döneme özel karar · Bilgi  
  Öğrencisi OBS'te görünmeyen derslerin sayısı elle girilir (ELLE_SAYI: Theory of International Trade 15 vb.). International Finance'in öğrenci sayısı bilinmiyor: sitede 'Belirtilmemiş', öğrenci çakışması denetlenemiyor.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:42-43, 345-347; kod/Belgeler/Devir Notu.md:144_
- **V13. Dersi fiilen almayan bölüm** · Bu döneme özel karar · Bilgi  
  Kullanıcı bazı bölümlerin dersi fiilen almadığını söyledi; bu gruplar beklenmez (Bölgesel Çalışmalar: Avrasya için YBS ve ETİC). Bu derste hücredeki sayılar önemsenmez, bölümler eşit paylaştırılır.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:44-48; kod/Belgeler/Devir Notu.md:107_
- **V14. Bölüme dahil etme** · Genel kural (her dönem) · Bilgi  
  Bir sınavın hangi bölüm sekmesinde görüneceği PDF satırlarına göre belirlenir; PDF satırı yoksa OBS'te en az 3 öğrencisi olan bölümler.  
  _Kaynak: kod/Yöntem/kod/6_bolum_programi.py:75, 97; kod/Belgeler/Devir Notu.md:99_
- **V15. Kişisel veri** · Genel kural (her dönem) · Bilgi  
  Öğrenci numarası ve adı içeren dosyalar (Öğrenci Dağılımı, Çakışma Çiftleri) paylaşılmaz; Belgeler/ ve Çıktılar/ GitHub'a gitmez. Formlara yalnız toplam sayı yazılır.  
  _Kaynak: kod/Yöntem/kod/kaynaklar.py:9; kod/Yöntem/kod/0_hoca_formu.py:11; kod/Yöntem/kod/5_yerlestir.py:1190; kod/README.md_
- **V16. Serbest metin talepler** · Genel kural (her dönem) · Bilgi  
  Hoca taleplerinde tarih/saat serbest metindir ('Perşembe 12-15', 'sabah'); belirsizler sorulur. Talep dosyasının sütun düzeni dönemden döneme değişebilir.  
  _Kaynak: kod/Yöntem/REHBER.md:108-110; kod/Yöntem/kod/1_dersleri_yukle.py:208-239_
- **V17. Dosya tuzakları** · Genel kural (her dönem) · Bilgi  
  Excel açıkken yazılamaz (kod '(yeni)' adıyla kaydeder). SharePoint formu canlıdır: üstüne dosya yüklemek cevapları siler.  
  _Kaynak: kod/Yöntem/REHBER.md:113; kod/Belgeler/Devir Notu.md:33, 132_

## 8. Yayından sonra gelen değişiklikler

- **SD1. En az değişiklik** · Genel kural (her dönem) · Yumuşak  
  Yayınlanmış programa değişiklik gelince program baştan kurulmaz. Değişen sınav önce eski yerinde denenir; olmazsa en yakın uygun saate taşınır (gün değişimi 25, saat farkı başına 4 ceza); hâlâ yer yoksa en çok 2 engelleyen sınav kaydırılır. Taşınma nedeni raporlanır, bütün dosyalar birlikte güncellenir.  
  _Kaynak: kod/Yöntem/kod/4_senaryo.py:3-12, 28, 118; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 45_
- **SD2. Değiştirilemez sınavlar** · Genel kural (her dönem) · Sert  
  Başlamış/yapılmış sınavlar ve kullanıcının kilitlediği sınavlar yerinden oynatılmaz, gözetmeni değişmez, yer açmak için taşınmaz. Hiçbir sınav geçmiş bir saate taşınmaz. Uygulanamayan değişiklik 'uygulanamadı' diye raporlanır.  
  _Kaynak: kod/Yöntem/kod/4_senaryo.py:14-17, 89-99, 193, 263; kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 46_
- **SD3. Gözetmenler korunur** · Genel kural (her dönem) · Yumuşak  
  Değişmeyen görevler kişisiyle korunur; değişen görevde önce eski kişi denenir, olmazsa yalnız o görev yeniden atanır.  
  _Kaynak: kod/Yöntem/kod/4_senaryo.py:10-11, 252-270_
- **SD4. Elle değişikliklerin kaydı** · Genel kural (her dönem) · Bilgi  
  Kullanıcı dosyada elle değişiklik yaparsa farklar listelenir, Devir Notu'na yazılır, onaylanırsa koda işlenir (ELLE_GRUP, KILIT vb.); yoksa yeniden üretimde ezilir. Yeni rapor dosyası üretilmez, mevcut dosyaya sayfa eklenir.  
  _Kaynak: kod/Belgeler/Devir Notu.md:121-122_
- **SD5. Son değişiklikler kutusu** · Genel kural (her dönem) · Bilgi  
  Her sınav veya gözetmen değişikliğinde 'Son değişiklikler' listesinin en üstüne bir satır eklenir.  
  _Kaynak: kod/OKU-BENI.md:18; kod/Yöntem/degisiklikler.json; VERI-BICIMI.md:132-161_

## 9. Bu dönemin kişiye ve derse özel kararları (Kasım 2026 vize)

- **K1. Meysure Evren Çelik Sütiçer** · Bu döneme özel karar · Sert  
  5 dersi (2023G2005, 2023G3009, 2023G3007, 2023G4009, 20G1009) kendi aralarında aynı bölüm-yarıyıl ve aynı hoca kuralından muaf; hepsi Salı; aynı oturumdakiler aynı derslikte. Ortak öğrencisi olanlar yine ayrı oturumda (Dijital Pazarlama 2 ile Arama Motoru'nun 8 ortak öğrencisi).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:82-83, 354-356, 641-667; kod/Belgeler/Devir Notu.md:38_
- **K2. Dikran Zenginkuzucu** · Bu döneme özel karar · Sert  
  Perşembe sınavı yok (20 Ekim); öncelikli hoca. International Law-I / Uluslararası Hukuk I birleşik, Çarşamba, aynı sınıf (Çarşamba 12:00 6D4). Hoca gözetmen istedi, öğrenci <30: onaylı.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:40, 65, 71-72; kod/Belgeler/Devir Notu.md:44-46_
- **K3. Derivatives and Risk Management (Sudi Apak)** · Bu döneme özel karar · Sert  
  Kodda Salı 09:00, yalnız 6D5 sabit; canlı veride Salı 10:00 6D5 (bkz. C12). Hoca gözetmen istedi, öğrenci <30: onaylı.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:74-75; kod/Belgeler/Devir Notu.md:41, 46; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx satır 27_
- **K4. İşletmeye Giriş** · Bu döneme özel karar · Bilgi  
  Cuma 12:00 sabiti 20 Ekim'de kaldırıldı (Zekeriya Şahin'in izin günü Cuma). Perşembe 11:00, 6 derslik. Ali Bakın bir dersliğe kendisi girer. Ali Bakın'ın 'lab' cevabı yok sayıldı.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:41; kod/Belgeler/Devir Notu.md:41, 43; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx satır 12_
- **K5. Hoca izin düzeltmeleri** · Bu döneme özel karar · Sert  
  Misagh Hajiamiri ve Ali Emre Eldem: izin Pazartesi (formdaki 5 gün geçersiz). Esma Görkem Ersoy'un hafta sonu girişleri yok sayıldı.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:40; kod/Belgeler/Devir Notu.md:45_
- **K6. Ufuk Erol'un dersleri** · Bu döneme özel karar · Sert  
  Ufuk Erol'un derslerine Misagh Hajiamiri girer; bu dersler Pazartesi hariç herhangi gün, ders saati talebi yok.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:80-81; kod/Belgeler/Devir Notu.md:45_
- **K7. Erdinç Gülbaş** · Bu döneme özel karar · Sert  
  Perşembe ve Cuma sınav yok (sert); 17:00 tercih (yumuşak). Consumer Behaviour ve Brand Management sınavsız (ödev).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:76-78; kod/Belgeler/Devir Notu.md:45_
- **K8. Alperen Şahin** · Bu döneme özel karar · Sert  
  Perşembe 15:00-18:00 dolu (başka fakültede ders).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:79; kod/Belgeler/Devir Notu.md:45_
- **K9. Gözetmen onaylı küçük sınıflar** · Bu döneme özel karar · Bilgi  
  Hoca gözetmen istedi ve öğrenci <30: onaylananlar Zenginkuzucu (2 ders), Apak (Derivatives), Telli (Neuro-Marketing), Doğruel (Veri Madenciliği). 'Kendim gireceğim' deyip 30+ öğrencisi olanlara da gözetmen (Devir Notu; uygulamada değişti, bkz. C5).  
  _Kaynak: kod/Belgeler/Devir Notu.md:46; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx satır 22-37_
- **K10. Kullanıcının eklediği gözetmenler** · Bu döneme özel karar · Bilgi  
  Dış Ticaret İşlemleri Muhasebesi (Alabayır) ve Maliyet Muhasebesi (Yaşar): 1'er gözetmen. 2 Kasım: Political Structure and Life in Turkey-I → Melih Mert Oskay; Economics of Development → Merve Sevinç Sakar. Gümrük Mevzuatı → Şeyma Sertçelik 6D1; Bölgesel Çalışmalar: Avrasya → Melih Mert Oskay 6D3. Dijital Muhasebe Uygulamaları (Sektör Kampüste, Salı 11:00 6A1) → Hilal Önge.  
  _Kaynak: kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Kontrol; kod/Yöntem/degisiklikler.json; kod/Belgeler/Devir Notu.md:147-148_
- **K11. Laboratuvar sınavları** · Bu döneme özel karar · Bilgi  
  Ülker Başar'ın 5 dersi (Algoritma ve Programlama 1, Excel VBA, Python, Veri Yapıları, Web Programlama) 90 dk, kullanıcının yerleştirdiği okul laboratuvarlarında.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:1375-1380; kod/Belgeler/Devir Notu.md:43, 105_
- **K12. İktisada Giriş I** · Bu döneme özel karar · Bilgi  
  Cuma 15:00, 3A1 + 3A3 + 3A5 (okul dosyası). Hocanın (Tuğba Koyuncu Çakmak) izin günü Cuma ama sınavı okul koydu: bilerek ihlal.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:1367-1369; kod/Belgeler/Devir Notu.md:104, 171_
- **K13. Sosyal Bilimler için Matematik I** · Bu döneme özel karar · Bilgi  
  Cuma 16:00-18:00 (2 saat), 3A6 + 4A3 + 4A4. Hoca İstatistik ile aynı (Betül Öztel).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:1370-1372; kod/Belgeler/Devir Notu.md:146-147, 169_
- **K14. İstatistik** · Bu döneme özel karar · Bilgi  
  2 saat, Cuma 12:00-14:00, 6A1 + 6D1 + 6D3 + 6D5. Cuma 15-17/16-18 İktisada ve SBM ile ortak öğrenci yüzünden elendi.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:1385; kod/Belgeler/Devir Notu.md:170, 175-176_
- **K15. Sosyolojide Temel Kavramlar** · Bu döneme özel karar · Bilgi  
  Sosyoloji bölümü isteğiyle Cuma 10:00-11:00, 3A5-3A6-3D6-3D7, onların öğrencileriyle ortak (iki ayrı sınav reddedildi). 60 dk.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:1373-1374; kod/Belgeler/Devir Notu.md:156_
- **K16. Introduction to Economics-I** · Bu döneme özel karar · Bilgi  
  Dersi İlknur Şimşek veriyor (Bayraktar değil). İşletme İng. + SBUİ İng. + ECF tek sınav, Çarşamba 13:00 6A1 (34 öğrenci).  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:178-180; kod/Yöntem/kod/6_bolum_programi.py:68; kod/Belgeler/Devir Notu.md:138, 153_
- **K17. International Finance** · Bu döneme özel karar · Bilgi  
  Bayraktar'ın 'Tourism Economics' dersi yerine; bütün İngilizce bölümler; öğrenci sayısı bilinmiyor; Perşembe 10:00 6A2, hoca girer. Tourism Economics sınavsız.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:181, 345-347; kod/Yöntem/kod/6_bolum_programi.py:69; kod/Belgeler/Devir Notu.md:139-144_
- **K18. Kullanıcının elle yerleştirdiği diğer sınavlar** · Bu döneme özel karar · Bilgi  
  Diplomasi Tarihi I + Diplomatic History I birleşik Cuma 16:00 6A1 (Eldem'e haber); Havaalanı Donanım ve Faaliyetleri Perşembe 16:00 6D4 (9 öğrencisi İktisada ve SBM'yi de alıyor, Cuma'dan uzak tutuldu); Hava Trafik Hizmetleri Salı 14:00 6D3; Yer Hizmetleri Salı 10:00 6A2. Aşama 4'ün 8 sınavı da kullanıcı tarafından yerleştirildi.  
  _Kaynak: kod/Belgeler/Devir Notu.md:96, 157, 175_
- **K19. Önemsiz kabul edilen uyarılar** · Bu döneme özel karar · Bilgi  
  ÇAP ve aynı bölüm-yarıyıl uyarıları, öğrenci o dersleri birlikte almıyorsa (ortak öğrenci 0) önemsiz sayıldı: Liman ve Terminal ↔ Temel Harekat, Lojistikte Kullanılan Belgeler ↔ Havacılık Yönetiminde Güncel Yaklaşımlar, Arama Motoru ↔ HYGY, Yer Hizmetleri. 3 ardışık sınav uyarıları da önemsiz sayıldı. Introduction to Economics-I'in 6D4'te +9 esnemesi bilinçli kabul edildi (sonra taşındı).  
  _Kaynak: kod/Belgeler/Devir Notu.md:106, 129, 138, 157_
- **K20. Geçerli gözetmen listesi** · Bu döneme özel karar · Bilgi  
  Liste 2 (herkes, 14 kişi) geçerli; Liste 1 (Seda ve Kadriye hariç) kullanılmayacak (23 Ekim).  
  _Kaynak: kod/Belgeler/Devir Notu.md:143_
- **K21. Gözetmen izin günleri** · Bu döneme özel karar · Sert  
  Seda Emir: Pazartesi + Cuma. Melih Mert Oskay: Salı (az güne toplansın). Mehmet Deniz Nalbantoğlu: Perşembe + Cuma. Ozan Atalay, Taha Gümüş, Şeyma Sertçelik, Elif Nur Eken, Tunahan Başoğlu, Merve Sevinç Sakar: Çarşamba. Kadriye Giray, Hilal Önge, Begüm İnanç, Tahsin Mert Saygın: Pazartesi. Duygu Yayla Eldem: Cuma. ('Ad / gün' yazımı = izin günü, kullanıcı onayı 22 Ekim.)  
  _Kaynak: kod/Yöntem/izinler.json; kod/Belgeler/Devir Notu.md:112; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Gözetmen Yükü_
- **K22. Kendi sınavına giren gözetmenler** · Bu döneme özel karar · Sayım  
  Elif Nur Eken kendi 3 sınavına (Ticari Örgütler, Uluslararası Finansman, Theory of International Trade), Duygu Yayla Eldem kendi 2 sınavına (History'de bir derslik + Siyaset Psikolojisi) girer; yüke dahil.  
  _Kaynak: kod/Belgeler/Devir Notu.md:112; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Kontrol_
- **K23. SBF gözetmenlikleri** · Bu döneme özel karar · Bilgi  
  SBF resmi listesine göre: Merve Sevinç Sakar Salı 12:00 Hemşirelik Biyokimya (3A5); Mehmet Deniz Nalbantoğlu + Begüm İnanç Salı 12:00 Biyokimya (3A6); Hilal Önge Çarşamba 14:00 Hemşirelik Mikrobiyoloji (12A1); Melih Mert Oskay Cuma 12:00 Hemşirelik Fizyolojisi (3A3). Diğer SBF istekleri (09:00'dakiler dahil) geri çevrildi.  
  _Kaynak: kod/Belgeler/Devir Notu.md:151, 172_
- **K24. Üniversite ortak seçmeli gözetmenlikleri** · Bu döneme özel karar · Bilgi  
  Çarşamba 04.11 11:00: Mehmet Deniz Nalbantoğlu → Türk İşaret Dili (3A1); Ozan Atalay + Şeyma Sertçelik → Temel İlk Yardım (3A3); Begüm İnanç → Temel İlk Yardım (3A5).  
  _Kaynak: kod/Belgeler/Devir Notu.md:161-163_
- **K25. Turkish Language I** · Bu döneme özel karar · Bilgi  
  Programda Pazartesi 15:00, 6A2 + 6D4 (39 öğrenci). Kullanıcı kararıyla (2 Kasım) bilerek gözetmen atanmadı; panel bu sınav için uyarı vermez.  
  _Kaynak: kod/Yöntem/kod/9_panel_uret.py:31, 83; git 2318d2a; veri.json_
- **K26. Diğer kullanıcı kararları (20-21 Ekim)** · Bu döneme özel karar · Bilgi  
  Para ve Bankacılık tek hoca. 'Günde en fazla 2 sınav' kuralı gerek yok. Sınıf düzeltmeleri: Terörizm ve İstihbarat / Terrorism and Intelligence 3, Davranışsal Finans 3, Managerial Leadership 4, Current Issues 3, Örgütsel Davranış Araştırmaları 2, Theory of International Trade 3, Innovation Management 4. Dijital Muhasebe Uygulamaları bölümleri UTF ve YBS.  
  _Kaynak: kod/Belgeler/Devir Notu.md:56, 99; kod/Yöntem/kod/6_bolum_programi.py:53-70_
- **K27. Açık kalan: Python ↔ Dijital İşletmecilik** · Bu döneme özel karar · Bilgi  
  22 Ekim: 'Python Perşembe 16:00'da kalır, Dijital İşletmecilik'in yeri değişecek' denmiş; sonrasında yapıldığına dair kayıt bulunamadı (belirsiz).  
  _Kaynak: kod/Belgeler/Devir Notu.md:106_

## 10. Site ve panel kuralları

- **W1. 'Gerekmiyor' yazımı** · Genel kural (her dönem) · Bilgi  
  Derslikte gözetmen yoksa veri 'Gerekmiyor' yazar; sitede 'Dersin hocası (gözetmen gerekmiyor)' görünür. Hoca kendi sınavında gözetmen sayılıyorsa 'Ad Soyad (dersin hocası)'.  
  _Kaynak: VERI-BICIMI.md:91-95; kod/Yöntem/kod/8_site_uret.py:137-141, 228-229_
- **W2. Panel uyarısı** · Bu döneme özel karar · Bilgi  
  Panelde 2+ derslikli olup hiçbir dersliğinde gözetmen olmayan sınav kırmızı uyarı alır. Başka birim kayıtları ve bilerek gözetmensiz bırakılanlar (GOZETMENSIZ: Turkish Language I) hariç.  
  _Kaynak: kod/Yöntem/kod/9_panel_uret.py:31, 80-83; kod/Yöntem/panel_sablonu.html:199-223_
- **W3. Düzenle'de gözetmen denetimi** · Genel kural (her dönem) · Sert  
  Sitede sınav düzenlenirken her gözetmen için denetlenir: aynı saatte başka sınavda gözetmen mi, o saatte kendi dersinin sınavı var mı, izinli mi, aynı sınavda iki derslikte mi. Biri bile varsa kayıt yapılmaz. Sınavda zaten kayıtlı gözetmen, gün/saat değişmedikçe yeniden denetlenmez.  
  _Kaynak: VERI-BICIMI.md:183-192; kod/Yöntem/site_tasarimi.html:2319-2373_
- **W4. Gözetmen önerme sırası** · Genel kural (her dönem) · Yumuşak  
  Gözetmen seçme penceresi o saatte müsait olanları en az görevliden en çoğa sıralar. Panelde uygun gözetmenler: önce sorunsuzlar (öncesi/sonrası boş, 3 ardışık saat olmayan), sonra yükü az olanlar; 3 ardışık saat olacaksa uyarır.  
  _Kaynak: kod/Yöntem/site_tasarimi.html:2436-2460; kod/Yöntem/panel_sablonu.html:226-247; index.html:1155_
- **W5. Sınav notları** · Genel kural (her dönem) · Bilgi  
  Birden çok derslik varsa 'N dersliğe bölündü'; 50 dakikadan uzunsa '60/90/120 dakika'; başka birim kayıtlarında 'Başka fakülte' ya da 'Üniversite ortak seçmeli' notu.  
  _Kaynak: VERI-BICIMI.md:75; kod/Yöntem/kod/8_site_uret.py:145-149, 168_
- **W6. Sayımlar** · Genel kural (her dönem) · Sayım  
  Sitedeki sınav sayısı (examCount) yalnız İYBF sınavlarını sayar; başka birimlere verilen gözetmenlik kayıtları sayılmaz.  
  _Kaynak: VERI-BICIMI.md:44, 124; kod/Yöntem/kod/8_site_uret.py:152, 174_
- **W7. Derslik sırası** · Genel kural (her dönem) · Bilgi  
  Sınav kartında önce 3. kat derslikleri, sonra diğerleri; her grup kendi içinde alfabetik.  
  _Kaynak: VERI-BICIMI.md:87; kod/Yöntem/kod/8_site_uret.py:132_
- **W8. İzin bilgisi sitede** · Genel kural (her dönem) · Bilgi  
  Gözetmen izinleri sitede yalnız ad ve gün olarak tutulur (başka kişisel bilgi yazılmaz).  
  _Kaynak: VERI-BICIMI.md:163-181; kod/Yöntem/izinler.json_
- **W9. Siteden yapılan düzenlemeler** · Genel kural (her dönem) · Bilgi  
  Motoru (8_site_uret.py) çalıştırmadan önce sitede yapılan 'düzenleme' commit'leri kontrol edilmeli ve önce Excel kaynaklarına işlenmeli; yoksa yeni veri bu düzenlemelerin üzerine yazar.  
  _Kaynak: VERI-BICIMI.md:251-258; kod/Yöntem/kod/8_site_uret.py:260-261_
- **W10. Gizlilik ve şifre** · Genel kural (her dönem) · Bilgi  
  Panel şifresi yüklenmez; boşluk ve harf büyüklüğü fark etmez. Sitedeki şifreler yalnız göz önünden saklar; gerçekten gizli bilgi siteye konmaz.  
  _Kaynak: kod/OKU-BENI.md:19; kod/Yöntem/kod/9_panel_uret.py:122; kod/Yöntem/REHBER.md:101-102_
- **W11. Yayın sırası** · Genel kural (her dönem) · Bilgi  
  7_gozetmenlik_formati.py → 9_panel_uret.py → 8_site_uret.py; çıktılar index.html ve panel/index.html olarak yüklenir. Yüklemeden önce depo güncellenir (git pull). Önbellek için adrese ?v=N eklenir.  
  _Kaynak: kod/OKU-BENI.md:5-10, 20-21; kod/Belgeler/Devir Notu.md:199_

## 11. Çelişkiler ve belirsizlikler

Kaynaklar arasında birbirini tutmayan ya da açık olmayan noktalar.

- **X1. Ardışık sınav kuralı iki farklı biçimde.** Şablon/REHBER: bir bölüm-yarıyıl grubunun kendi dersleri günde en fazla 2 arka arkaya (alttan hariç). Güz kodu: öğrenci bazında 3 ardışık oturum yok (alttan dahil), sığmazsa gevşetilir; kullanıcı ayrıca bazı 3 ardışık uyarılarını 'önemsiz' saydı.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 21; kod/Yöntem/kod/5_yerlestir.py:493-511; kod/Belgeler/Devir Notu.md:42, 106_
- **X2. Derslik kapasiteleri tutarsız.** Şablon ve Kod Anahtarı (Bahar): 6A1 24, 6A2 24, 6D1 15, 6D3 15, 6D4 20, 6D5 20; 3A1 80, 3A3 80, 3A5 70, 3A6 60. Güz: 6A1 35, 6A2 33, 6D1 17, 6D3 23, 6D4 25, 6D5 23; 3A1 90, 3A3 85, 3A5 60, 3A6 50. Okul dosyası başlığı 3A3 için 107 (tam) yazıyor. Hangi değerlerin kalıcı olduğu belirsiz.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 5; kod/Yöntem/Kod Anahtari.txt; kod/Yöntem/kod/5_yerlestir.py:30; kod/Yöntem/kod/8_site_uret.py:56_
- **X3. Esneme sınırları.** Şablon: kapasite ±6 kişi esnek. Güz: +5 / +8 / +20. Kodda ESNEME_BUYUK = 10 tanımlı ama büyük derslerde esneme 20'ye kadar deneniyor (sabit kullanılmıyor). 6. kat dosyası başlığında '+5 esneme' yazıyor.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 5; kod/Yöntem/kod/5_yerlestir.py:34-37, 463_
- **X4. 3. kat kuralı.** Şablon: 60'tan kalabalık sınav 3. kata, hoca talebinden önce. Güz: 3. kata kullanıcı onayı olmadan yerleşim yok; İktisada ve SBM okul tarafından 3./4. kata kondu. Devir Notu ayrıca bu iki dersin 6. kata da sığabileceğini yazıyor.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 10; kod/Belgeler/Devir Notu.md:39, 129_
- **X5. Gözetmen ihtiyacı: ≥30 kuralı uygulanmıyor.** Kural: 30+ öğrenci → gözetmen; Devir Notu 22 Ekim '30+ öğrencili 9 tek derslikli sınav' eklendiğini yazıyor. Liste 2 Kontrol ve OKU-BENI ise 'yalnız 2+ derslik listesi' diyor. Canlı veride 30+ öğrencili birçok tek derslikli sınav gözetmensiz: Pazarlamaya Giriş 31, Business Finance 35, Tedarik Zinciri Yönetimi 40, Endüstri 4.0 34, Introduction to Economics-I 34, Liman ve Terminal 32, Kombine Taşımacılığı 32, Lojistikte Modelleme 33, Havacılık İngilizcesi-I 30, Sivil Havacılık 30, lab sınavları (30-38).  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 30; kod/Belgeler/Devir Notu.md:46, 111; kod/OKU-BENI.md:16; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Kontrol; veri.json_
- **X6. Derslik başına 1 gözetmen kuralı.** Kural her dersliğe 1 gözetmen diyor; kullanıcı listesinde bazı çok derslikli sınavlarda (Küresel Rekabetçilik, Bölgesel Çalışmalar, Havacılıkta Stratejik Yönetim, Gümrük Mevzuatı) 2 derslik için 1 gözetmen var, diğer dersliğe hoca giriyor.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 32; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx satır 3, 5, 10, 15_
- **X7. Uzun sınavın görev sayısı.** Bahar v2 kodu (2_programi_kur.py) 90 dakikalık sınava gireni 1 görev sayıyor; Güz kararı ve site 2 görev sayıyor.  
  _Kaynak: kod/Yöntem/kod/2_programi_kur.py:621-622; kod/Yöntem/kod/7_gozetmenlik_formati.py:40, 79_
- **X8. Gözetmenin üst üste 3 görevi.** Şablonda sert; Güz'de cezaya çevrildi. Liste 2 Kontrol'e göre 4 kişide 3 ardışık saat var (Taha Gümüş, Kadriye Giray, Begüm İnanç: Cuma 15-18; Melih Mert Oskay: Cuma 10-13).  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 38; kod/Belgeler/Devir Notu.md:147, 151; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Kontrol_
- **X9. İzin gününde görev.** Ozan Atalay ve Şeyma Sertçelik'in izin günü Çarşamba, ama Çarşamba 11:00 ortak seçmeli (Temel İlk Yardım) görevi verilmiş. Devir Notu 'kullanıcı onayı bekleniyor' diyor; onay kaydı bulunamadı.  
  _Kaynak: kod/Yöntem/izinler.json; kod/Belgeler/Devir Notu.md:163; veri.json_
- **X10. İstatistik gözetmenleri.** Devir Notu (30 Ekim): Ozan, Şeyma, Kadriye, Elif Nur Eken + 4 takas. Liste 2 Kontrol '30 Ekim geri alma' ve canlı veri: Taha Gümüş, Hilal Önge, Kadriye Giray, Tahsin Mert Saygın. Devir Notu'nun bu kısmı eskimiş.  
  _Kaynak: kod/Belgeler/Devir Notu.md:177; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Kontrol; veri.json_
- **X11. Büyük salonlarda kapasite aşımı.** Koddaki dağılıma göre İktisada Giriş I'de 3A5'te 90 öğrenci var (sınav kapasitesi 60); SBM'de 3A6'da 52 (kap. 50), 4A4'te 59 (kap. 50). Devir Notu'nda İktisada için önerilen dağılım farklıydı (3A1 İŞL 46 + HAV 44 …). Hangisinin gerçek olduğu belirsiz.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:1367-1372; kod/Yöntem/kod/8_site_uret.py:56; kod/Belgeler/Devir Notu.md:104; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx alt not_
- **X12. Derivatives saati.** Kodda SABIT Salı 09:00 (6D5); 2+ derslik listesi ve canlı veri Salı 10:00 6D5.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:74; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx satır 27; veri.json_
- **X13. Sektör Kampüste dersleri.** Devir Notu 'hocasız 2 Sektör Kampüste dersi programa girmez' diyor; Dijital Muhasebe Uygulamaları (Sektör Kampüste) programda, Hilal Önge gözetmen.  
  _Kaynak: kod/Belgeler/Devir Notu.md:10, 148_
- **X14. Turkish Language I.** Ortak ders kodları OKUL_YAPAR'da ve Devir Notu 'karar bekleniyor' diyor; canlı programda Pazartesi 15:00 (39 öğrenci, 2 derslik) gözetmensiz. Kimin yaptığı ve gözetmensiz kararının gerekçesi yazılı değil.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:50, 804-805; kod/Belgeler/Devir Notu.md:47, 56; kod/Yöntem/kod/9_panel_uret.py:31_
- **X15. Bölünen grupta sıralama.** Kod ve Öğrenci Dağılımı açıklaması öğrenci NUMARASI sırası diyor; aynı fonksiyonun açıklama satırı 'soyad (sonra ad) sırası' diyor.  
  _Kaynak: kod/Yöntem/kod/5_yerlestir.py:760, 774, 1191_
- **X16. Öğrenci sayısı kaynağı.** Şablon: hocanın talepte yazdığı sayı esas, yoksa OBS. Güz: OBS kayıt sayısı esas; hocanın ek öğrenci tahminleri eklenmedi.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 26; kod/Belgeler/Devir Notu.md:124_
- **X17. Hoca formu metni ile uygulama.** Form '30'dan az öğrencili derse gözetmen atanmaz' diyor; ama onaylı istisnalar var (Derivatives 2 öğrenci, Economics of Development 11, Political Structure 5, Neuro-Marketing 10 gözetmenli).  
  _Kaynak: kod/Yöntem/kod/0_hoca_formu.py:42-43; veri.json; kod/Yöntem/degisiklikler.json_
- **X18. SBUİ İngilizce ↔ Havacılık.** Kullanıcı bu çifti ÇAP yumuşak kuralından çıkardı ama kod ayırmıyor; yumuşak sayaç fazla uyarı veriyor.  
  _Kaynak: kod/Belgeler/Devir Notu.md:92; kod/Yöntem/kod/5_yerlestir.py:86_
- **X19. 4. kat gözetmen sayısı.** 3. kat için 2 gözetmen kuralı yazılı; 4. kat için 2 gözetmen yalnız 'varsayım' olarak geçiyor.  
  _Kaynak: kod/Yöntem/Yeni Dönem Şablonu.xlsx / Genel Kısıtlar, satır 33; kod/Sınav Çıktıları/2+ Derslikli Sınavlar (22.10.2026).xlsx alt not_
- **X20. '09:00 serbest'.** Devir Notu gözetmen atamasında '09:00 serbest' diyor; anlamı (09:00'da görev verilebilir mi, verilmez mi) açık değil (belirsiz).  
  _Kaynak: kod/Belgeler/Devir Notu.md:112; kod/Sınav Çıktıları/Gözetmen Atamaları - Liste 2 (herkes, 14 kişi).xlsx / Kontrol_

## 12. Finalde sorulması gerekenler

Final programına başlamadan komisyona ve hocalara sorulacaklar.

- **F1. Takvim.** Final haftasının tarihleri, tatil günleri; Çarşamba 09:00-12:00 yasağı finalde de geçerli mi?  
  _Kaynak: kod/Yöntem/REHBER.md:58; kod/Yöntem/kod/5_yerlestir.py:29_
- **F2. Derslikler.** 6. kat ve 3./4. kat derslik müsaitliği, salonların sınav kapasiteleri (X2), lab adları ve kapasiteleri; TÖMER sınıfları kullanılabilir mi?  
  _Kaynak: kod/Yöntem/REHBER.md:52, 59; kod/Belgeler/Devir Notu.md:43, 103_
- **F3. Hoca formu.** Form yeniden doldurulacak mı: sınav var mı, ders saatinde mi, süre, gözetmen, izin günü, lab, aynı anda yapılacak sınav, eksik bölüm.  
  _Kaynak: kod/Yöntem/REHBER.md:61-66; kod/Belgeler/2026-2027 Güz Vize - Hoca Bilgi Formu (Toplu) (1).xlsx / Yönerge_
- **F4. Kişiye özel kararlar.** Bölüm 9'daki kararlar (Zenginkuzucu Perşembe, Meysure Salı/aynı sınıf, Gülbaş Per-Cum, Alperen Şahin Per 15-18, Hajiamiri/Eldem Pazartesi, Erol dersleri, Derivatives sabiti, birleşik sınavlar) finalde de geçerli mi?  
  _Kaynak: Bölüm 9_
- **F5. Gözetmen listesi.** Gözetmen listesi, izin günleri, kişisel saat kısıtları, az güne toplama istekleri ve cinsiyet (K/E) bilgisi (3./4. kat eşleştirmesi için).  
  _Kaynak: kod/Yöntem/REHBER.md:60; kod/Belgeler/Devir Notu.md:112, 143_
- **F6. Gözetmen ihtiyacı kuralı.** 30+ öğrencili tek derslikli sınavlara gözetmen verilecek mi, yoksa yalnız 2+ derslikli sınavlara mı (X5)? Çok derslikli sınavda bir dersliğe hoca girebilir mi (X6)? 4. kat salonlarında 2 gözetmen mi (X19)?  
  _Kaynak: X5, X6, X19_
- **F7. Gözetmen ardışık saat.** Üst üste 3 saat gözetmenlik sert mi, cezalı mı (X8)? '09:00 serbest' ne demek (X20)?  
  _Kaynak: X8, X20_
- **F8. Görev sayımı.** 60 dakikalık SBF/ortak seçmeli/Sosyoloji görevleri 1 mi? Muafiyet sınavı görevi finalde de var mı, kaç saat ve kimlere?  
  _Kaynak: GS3, GS4_
- **F9. Okulun sınavları.** Okulun büyük salonda yaptığı sınavların (İktisada Giriş, SBM, Sosyolojide Temel Kavramlar) ve ortak derslerin (Türk Dili, Yabancı Dil, Atatürk İlkeleri) final tarihleri; Turkish Language I'i kim yapacak, gözetmen gerekecek mi (X14)?  
  _Kaynak: kod/Belgeler/Devir Notu.md:47, 104, 156_
- **F10. Eksik veri.** International Finance öğrenci sayısı; İngilizce 'Basic Concepts in Sociology' Sosyoloji'nin ortak sınavından etkileniyor mu; Sektör Kampüste dersleri sınav yapacak mı (X13)?  
  _Kaynak: kod/Belgeler/Devir Notu.md:144, 159_
- **F11. Esneme ve 3. kat.** +5 / +8 / +20 esneme sınırları ve '3. kata onaysız yerleşim yok' kuralı finalde de geçerli mi (X3, X4)?  
  _Kaynak: X3, X4_
- **F12. ÇAP.** ÇAP öğrenci listesi alınabilir mi? Alınamazsa Havacılık↔Lojistik ve E-Ticaret↔Havacılık sert kuralı sürecek mi (K19)?  
  _Kaynak: kod/Belgeler/Devir Notu.md:129, 133_
- **F13. Öğrenci ardışık sınav.** Öğrenci bazında '3 ardışık sınav yok' kuralı finalde de geçerli mi; günlük sınav sayısına sınır istenecek mi (X1)?  
  _Kaynak: kod/Belgeler/Devir Notu.md:42, 127_
- **F14. Başka birim istekleri.** SBF ve ortak seçmeli gözetmen istekleri gelecek mi; hangi saatler (09:00 dahil) kabul edilecek; izin gününe görev verilebilir mi (X9)?  
  _Kaynak: kod/Belgeler/Devir Notu.md:151, 163_
- **F15. Açık konular.** Python ↔ Dijital İşletmecilik (K27), Derivatives saati (X12), büyük salon dağılımı (X11).  
  _Kaynak: K27, X11, X12_

## Okunan kaynaklar

Kod: `kod/Yöntem/kod/0_hoca_formu.py`, `0b_cakisma_ciftleri.py`, `1_dersleri_yukle.py`, `2_programi_kur.py`, `4_senaryo.py`, `5_yerlestir.py`, `6_bolum_programi.py`, `7_gozetmenlik_formati.py`, `8_site_uret.py`, `9_panel_uret.py`, `kaynaklar.py`, `donem_ayarlari_ornek.py`. Belgeler: `kod/OKU-BENI.md`, `kod/README.md`, `kod/Yöntem/REHBER.md`, `kod/Yöntem/Kod Anahtari.txt`, `kod/Belgeler/Devir Notu.md`, `kod/Belgeler/Aşama 4 Seçenekleri.md`, `VERI-BICIMI.md`. Excel: `Yeni Dönem Şablonu.xlsx` (Genel Kısıtlar; Özel Kısıtlar boş), Hoca Bilgi Formu (Yönerge ve başlıklar), `2+ Derslikli Sınavlar`, `Gözetmen Atamaları - Liste 2` (Gözetmen Yükü, Kontrol, Atamalar başlığı), Bölüm programı (Sınıf Kontrol), derslik dosyaları (yalnız başlıklar). Site: `kod/Yöntem/panel_sablonu.html`, `kod/Yöntem/site_tasarimi.html`, `index.html`, `veri.json`, `kod/Yöntem/izinler.json`, `kod/Yöntem/degisiklikler.json`; git günlüğü. Öğrenci kişisel verisi içeren sayfalar açılmadı.

