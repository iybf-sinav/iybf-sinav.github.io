"""v2'yi ana sitenin güncel verisiyle eşitler: python3 v2/esitle.py (depo kökünden)
Ana siteden şu üç parça kopyalanır, v2'nin kendi değişikliklerine dokunulmaz:
sınav verisi (const DATA), Son değişiklikler kutusu, panel sürüm eki."""
import re

ana = open("index.html", encoding="utf-8").read().replace("\r\n", "\n")
v2 = open("v2/index.html", encoding="utf-8").read()


def parca(metin, desen):
    bulunan = re.findall(desen, metin, re.S)
    assert len(bulunan) == 1, desen
    return bulunan[0]


for desen in [r"    const DATA = .*?;\n",
              r'      <section class="degisiklik".*?</section>\n',
              r'panel/\?v=\d+"']:
    yeni = parca(ana, desen)
    eski = parca(v2, desen)
    v2 = v2.replace(eski, yeni)

open("v2/index.html", "w", encoding="utf-8").write(v2)
print("v2 eşitlendi")
