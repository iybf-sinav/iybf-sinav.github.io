"""v2'yi canlı siteyle eşitler (depo kökünden çalıştırın).
  python3 2627vizeprogrami/v2/esitle.py               v2'yi canlı sitenin tam kopyasına döndürür (v2'deki tasarım değişiklikleri silinir)
  python3 2627vizeprogrami/v2/esitle.py --sadece-veri yalnız sınav verisini (veri.json) ve e-postaları canlıdan kopyalar
Kopyada: deneme şeridi, sekme başlığında "[v2 Deneme]", düzenlemeler v2/veri.json'a yazılır, panel ../panel/ adresinden açılır,
boş bir "Yeni Özellikler" sekmesi eklenir.
v2/kurallar.json ve v2/KURALLAR.md silinmez; ama tam sıfırlamada Panel'in "Kurallar" alt sekmesi index.html'den gider (yeniden eklenmeli).
Sınav zarfı kayıtları (v2/veri.json "envelopes" alanı, yalnız v2'de):
  --sadece-veri  canlı veri kopyalanır ama v2/veri.json'daki "envelopes" alanı korunur (yeni dosyanın sonuna yazılır).
  seçeneksiz     tam sıfırlamada "envelopes" de silinir (v2 canlının birebir kopyasına döner); bu beklenen davranıştır."""
import json
import shutil
import sys

if "--sadece-veri" in sys.argv:
    try:
        zarflar = json.load(open("2627vizeprogrami/v2/veri.json", encoding="utf-8")).get("envelopes")
    except (OSError, ValueError):
        zarflar = None
    veri = json.load(open("2627vizeprogrami/veri.json", encoding="utf-8"))
    if zarflar:
        veri["envelopes"] = zarflar
        open("2627vizeprogrami/v2/veri.json", "w", encoding="utf-8", newline="\n").write(json.dumps(veri, ensure_ascii=False, indent=1) + "\n")
    else:
        shutil.copyfile("2627vizeprogrami/veri.json", "2627vizeprogrami/v2/veri.json")
    shutil.copyfile("2627vizeprogrami/epostalar.json", "2627vizeprogrami/v2/epostalar.json")
    print("v2 verisi canlıyla eşitlendi" + (" (zarf kayıtları korundu: %d)" % len(zarflar) if zarflar else ""))
    sys.exit()

shutil.copyfile("2627vizeprogrami/veri.json", "2627vizeprogrami/v2/veri.json")
shutil.copyfile("2627vizeprogrami/epostalar.json", "2627vizeprogrami/v2/epostalar.json")

h = open("2627vizeprogrami/index.html", encoding="utf-8").read().replace("\r\n", "\n")


def degistir(eski, yeni):
    global h
    assert h.count(eski) == 1, eski[:60]
    h = h.replace(eski, yeni)


degistir("<title>", "<title>[v2 Deneme] ")
degistir('<nav class="top-nav"',
         '<div style="padding:8px 16px;color:#fff;background:#b45309;text-align:center;font-weight:700;font-size:.9rem">'
         'DENEME SÜRÜMÜ (v2) · Asıl site: <a href="../" style="color:#fff">iybf-sinav.github.io</a></div>\n  <nav class="top-nav"')
degistir('const EDIT_FILE = "2627vizeprogrami/veri.json";', 'const EDIT_FILE = "2627vizeprogrami/v2/veri.json";')
degistir('const PANEL_URL = "../panel/?v=', 'const PANEL_URL = "../../panel/?v=')
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
open("2627vizeprogrami/v2/index.html", "w", encoding="utf-8").write(h)
print("v2 canlı sitenin kopyasına döndürüldü")
