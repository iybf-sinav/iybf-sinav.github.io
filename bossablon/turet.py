"""v2'deki kodu boş şablona ve final programına yayar (depo kökünden çalıştırın).
  python3 bossablon/turet.py          2627vizeprogrami/v2/index.html → bossablon/index.html ve 2627finalprogrami/index.html
  python3 bossablon/turet.py --denetle  dosyaları yazmaz; türetilen sayfa mevcut dosyalarla aynı değilse hata verir

Türetilen sayfa v2'nin aynısıdır, şunlar dışında:
  - deneme şeridi ("DENEME SÜRÜMÜ (v2)"), sekme başlığındaki "[v2 Deneme]" öneki ve v2'nin dönem varsayılanları yok
    (başlık ve sekme adı klasörün veri.json → meta alanlarından gelir);
  - Panel sekmesinde sahibin panel sayfası (iframe), Panel şifre kapısı ve "Yeni Özellikler" yok:
    Panel sekmesi doğrudan "Veriler" ile açılır, alt sekmeler Veriler | Kurallar;
  - Kurallar sayfasının açıklaması şablona göre (kurallar.json yalnız genel kurallarla başlar);
  - düzenleyici anahtarı ayrı tarayıcı anahtarında saklanır, zarf commit mesajında "v2" yok.
Düzenlemeler sayfanın klasöründeki dosyalara yazılır (veri.json, epostalar.json, kurallar.json); kod klasör adına bağlı değildir.
Yalnız index.html üretilir; veri.json, epostalar.json, kurallar.json ve OKU-BENI.md'ye dokunulmaz.
v2'de bu betiğin aradığı metinlerden biri değişirse betik durur (hangi metin olduğunu yazar); o zaman bu dosya güncellenmelidir."""
import re
import sys

KAYNAK = "2627vizeprogrami/v2/index.html"
HEDEFLER = ["bossablon/index.html", "2627finalprogrami/index.html"]

h = open(KAYNAK, encoding="utf-8").read().replace("\r\n", "\n")


def degistir(eski, yeni):
    global h
    assert h.count(eski) == 1, "v2'de bulunamadı ya da birden çok: " + eski[:80]
    h = h.replace(eski, yeni)


def sil_arasi(bas, son):
    """bas ile başlayan, son ile biten (son dahil) tek bölümü siler."""
    global h
    assert h.count(bas) == 1, "v2'de bulunamadı ya da birden çok: " + bas[:80]
    i = h.index(bas)
    j = h.index(son, i)
    h = h[:i] + h[j + len(son):]


# ---- başlık, deneme şeridi, dönem varsayılanları ----
degistir("<title>[v2 Deneme] 2026-2027 Güz Dönemi Vize Sınav Programı | İşletme ve Yönetim Bilimleri Fakültesi</title>",
         "<title>Sınav Programı | İşletme ve Yönetim Bilimleri Fakültesi</title>")
degistir('<p class="header-meta" id="app-meta">2026-2027 Güz Dönemi Vize Sınav Takip Uygulaması · 2–6 Kasım 2026</p>',
         '<p class="header-meta" id="app-meta">Sınav Takip Uygulaması</p>')
sil_arasi('  <div style="padding:8px 16px;color:#fff;background:#b45309;text-align:center;font-weight:700;font-size:.9rem">DENEME SÜRÜMÜ (v2)',
          "</div>\n")
degistir('''    const TITLE_PREFIX = "[v2 Deneme] ";                  // sekme başlığı öneki
    const DEFAULT_PROGRAM = "2026-2027 Güz Dönemi Vize";  // veri.json meta.programName yoksa
    const DEFAULT_PERIOD = "2–6 Kasım 2026";              // veri.json meta.period yoksa''',
         '''    const TITLE_PREFIX = "";      // sekme başlığı öneki
    const DEFAULT_PROGRAM = "";   // veri.json meta.programName yoksa
    const DEFAULT_PERIOD = "";    // veri.json meta.period yoksa''')

# ---- Panel: şifre kapısı, sahibin paneli (iframe) ve Yeni Özellikler yok ----
sil_arasi("    /* Panel'e tek şifreyle giriş (Değişiklik 7) */\n", ".view-toggle .panel-lock { margin-left: 8px; color: #b42318; }\n")
degistir('aria-controls="page-panel" aria-selected="false" data-page="panel">Panel</button>',
         'aria-controls="page-data" aria-selected="false" data-page="panel">Panel</button>')
sil_arasi('    <section class="page" id="page-panelgate"', "    </section>\n")
sil_arasi('    <section class="page" id="page-panel" ', "    </section>\n")
sil_arasi('    <section class="page" id="page-features"', "    </section>\n")
for satir in ['        <button type="button" data-subpage="panel" aria-pressed="false">Panel</button>\n',
              '        <button type="button" data-subpage="features" aria-pressed="false">Yeni Özellikler</button>\n',
              '        <button type="button" class="panel-lock" data-panel-lock>Paneli kilitle</button>\n']:
    assert h.count(satir) == 2, satir
    h = h.replace(satir, "")
degistir("    // Panel sayfasındaki alt sekmeler: Panel | Veriler | Kurallar | Yeni Özellikler (hepsi tek şifreyle açılır, Değişiklik 7)",
         "    // Panel sayfasındaki alt sekmeler: Veriler | Kurallar")
degistir('''      const app = pageName === "envelopes" ? "envelope" : "exam";''',
         '''      if (pageName === "panel" || pageName === "features") pageName = "data";   // şablonda Panel sekmesi Veriler ile açılır
      const app = pageName === "envelopes" ? "envelope" : "exam";''')
degistir('''      // Panel bölümleri şifre doğrulanana kadar açılmaz; yerine şifre kapısı görünür (Değişiklik 7)
      let shown = pageName;
      if (PANEL_PAGES.indexOf(pageName) !== -1 && !panelOpen) { panelTarget = pageName; shown = "panelgate"; }
''', "")
degistir('''String(button.dataset.page === (PANEL_PAGES.indexOf(pageName) !== -1 ? "panel" : pageName))''',
         '''String(button.dataset.page === (pageName === "features" || pageName === "data" || pageName === "rules" ? "panel" : pageName))''')
degistir('''        page.hidden = page.id !== "page-" + shown;''', '''        page.hidden = page.id !== "page-" + pageName;''')
degistir('''      if (shown === "panelgate") showPanelGate();
      if (shown === "panel") openPanel();
      if (shown === "rules") openRules();''', '''      if (pageName === "rules") openRules();''')
degistir('''    // ---- Panel sekmesi: panel/ sayfası kendi şifre ekranıyla açılır (şifre panelde sorulur) ----
    const PANEL_URL = "../../panel/?v=" + Math.floor(Date.now() / 600000);   // önbellek 10 dakikada bir yenilenir
''', "")
sil_arasi("    // ---- Panel'e tek şifreyle giriş (Değişiklik 7) ----\n", '''      frame.src = PANEL_URL;
    }

''')

# ---- Kurallar sayfası: şablon metinleri ----
degistir("<p>Sınav programının hangi kurallarla kurulduğu. Kurallar komisyonun yerleştirme kodundan ve belgelerinden derlendi. “Genel” her dönem geçerli kuraldır; “Bu dönem” Kasım 2026 vizesine özel karardır. Liste finalde gözden geçirilecek.</p>",
         "<p>Sınav programının kurulduğu genel kurallar (her dönem geçerli). Kurallar komisyonun yerleştirme kodundan ve belgelerinden derlendi; döneme özel kararlar bu klasörün kurallar.json dosyasına eklenebilir.</p>")
degistir('<p class="rules-doc">Belgenin tamamı: <a href=',
         '<p class="rules-doc">Kuralların derlendiği belge (2026-2027 Güz vizesi, döneme özel kararlar dahil): <a href=')
degistir("    // Panel > Kurallar alt sekmesi (Değişiklik 5): kurallar.json (v2/ içinde) ilk açılışta okunur",
         "    // Panel > Kurallar alt sekmesi: kurallar.json (bu klasörde; yalnız her dönem geçerli genel kurallarla başlar) ilk açılışta okunur")

# ---- küçük metinler ----
degistir("    // Başlık (Değişiklik 6): fakülte adı,", "    // Başlık: fakülte adı,")
degistir('''"v2 zarf: " + course''', '''"zarf: " + course''')
degistir('''    // Düzenlemelerin yazıldığı dosya sayfanın klasöründen türetilir: /2627vizeprogrami/v2/ → "2627vizeprogrami/v2/veri.json".''',
         '''    // Düzenlemelerin yazıldığı dosya sayfanın klasöründen türetilir: /bossablon/ → "bossablon/veri.json", /2627finalprogrami/ → "2627finalprogrami/veri.json".''')
degistir('''const EDITOR_KEY = "iybf-v2-duzenleyici-anahtar";''', '''const EDITOR_KEY = "iybf-duzenleyici-anahtar";''')
degistir('''if (typeof envelopeExams === "function") {   // v2: sınav zarfı takibi''', '''if (typeof envelopeExams === "function") {   // sınav zarfı takibi''')

# ---- denetim: v2'ye özgü hiçbir şey kalmamalı ----
for iz in ["DENEME SÜRÜMÜ", "[v2 Deneme]", "page-panelgate", "id=\"panel-frame\"", "id=\"page-features\"", "PANEL_PAGES", "PANEL_URL", "data-panel-lock",
           "showPanelGate", "openPanel", "iybf-v2-"]:
    assert iz not in h, "türetilen sayfada kaldı: " + iz
assert not re.search(r"\bv2 zarf\b", h)

if "--denetle" in sys.argv:
    farkli = [yol for yol in HEDEFLER if open(yol, encoding="utf-8").read() != h]
    if farkli:
        sys.exit("v2'den türetilen sayfa güncel değil: " + ", ".join(farkli) + " (python3 bossablon/turet.py çalıştırın)")
    print("türetilen sayfalar güncel")
    sys.exit()
for yol in HEDEFLER:
    open(yol, "w", encoding="utf-8", newline="\n").write(h)
print("yazıldı: " + ", ".join(HEDEFLER))
