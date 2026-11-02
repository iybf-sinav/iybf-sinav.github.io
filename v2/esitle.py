"""v2'yi canlı siteyle eşitler (depo kökünden çalıştırın).
  python3 v2/esitle.py               v2'yi canlı sitenin tam kopyasına döndürür (v2'deki tasarım değişiklikleri silinir)
  python3 v2/esitle.py --sadece-veri yalnız sınav verisini (veri.json) ve e-postaları canlıdan kopyalar
Kopyada: deneme şeridi, sekme başlığında "[v2 Deneme]", düzenlemeler v2/veri.json'a yazılır, panel ../panel/ adresinden açılır,
boş bir "Yeni Özellikler" sekmesi eklenir."""
import shutil
import sys

shutil.copyfile("veri.json", "v2/veri.json")
shutil.copyfile("epostalar.json", "v2/epostalar.json")
if "--sadece-veri" in sys.argv:
    print("v2 verisi canlıyla eşitlendi")
    sys.exit()

h = open("index.html", encoding="utf-8").read().replace("\r\n", "\n")


def degistir(eski, yeni):
    global h
    assert h.count(eski) == 1, eski[:60]
    h = h.replace(eski, yeni)


degistir("<title>", "<title>[v2 Deneme] ")
degistir('<nav class="top-nav"',
         '<div style="padding:8px 16px;color:#fff;background:#b45309;text-align:center;font-weight:700;font-size:.9rem">'
         'DENEME SÜRÜMÜ (v2) · Asıl site: <a href="../" style="color:#fff">iybf-sinav.github.io</a></div>\n  <nav class="top-nav"')
degistir('const EDIT_FILE = "veri.json";', 'const EDIT_FILE = "v2/veri.json";')
degistir('const PANEL_URL = "panel/?v=', 'const PANEL_URL = "../panel/?v=')
degistir('data-page="panel">Panel</button>',
         'data-page="panel">Panel</button>\n      <button class="tab-button" id="tab-features" role="tab" '
         'aria-controls="page-features" aria-selected="false" data-page="features">Yeni Özellikler</button>')
degistir("  </main>", '''    <section class="page" id="page-features" role="tabpanel" aria-labelledby="tab-features" hidden>
      <div class="page-heading">
        <div>
          <h2>Yeni Özellikler</h2>
          <p>Bu deneme sürümünde (v2) asıl siteden farklı olarak eklenenler. Beğenilenler asıl siteye taşınır.</p>
        </div>
      </div>
      <ol class="feature-list">
        <li>Henüz yeni özellik yok; v2 şu an canlı sitenin kopyası.</li>
      </ol>
    </section>
  </main>''')
degistir('panel: "panel" };', 'panel: "panel", features: "yeni-ozellikler" };')
degistir('''      "ana-sayfa": "home"
    };''', '''      "ana-sayfa": "home",
      "yeni-ozellikler": "features"
    };''')
open("v2/index.html", "w", encoding="utf-8").write(h)
print("v2 canlı sitenin kopyasına döndürüldü")
