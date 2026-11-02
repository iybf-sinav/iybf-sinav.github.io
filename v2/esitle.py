"""v2'yi ana sitenin güncel verisiyle eşitler: python3 v2/esitle.py (depo kökünden)
Site verisi v2/veri.json'a yazılır (biçim: v2/VERI-BICIMI.md); v2/index.html'de yalnız panel sürüm eki güncellenir.
Kaynak: kökte veri.json varsa o; yoksa ana sitedeki gömülü sınav verisi (const DATA)
+ kod/Yöntem/degisiklikler.json (Son değişiklikler).
Gözetmen izin günleri (proctorAvailability) kaynakta yoksa mevcut v2/veri.json'dakiler korunur."""
import html
import json
import os
import re

ana = open("index.html", encoding="utf-8").read().replace("\r\n", "\n")
v2 = open("v2/index.html", encoding="utf-8").read()


def parca(metin, desen):
    bulunan = re.findall(desen, metin, re.S)
    assert len(bulunan) == 1, desen
    return bulunan[0]


def son_degisiklikler():
    """degisiklikler.json; yoksa ana sitedeki Son değişiklikler kutusundan okunur (en yeni üstte)."""
    yol = os.path.join("kod", "Yöntem", "degisiklikler.json")
    if os.path.exists(yol):
        return [{"tarih": g["tarih"], "tur": g["tur"], "metin": g["metin"]} for g in json.load(open(yol, encoding="utf-8"))]
    kutu = re.search(r'<section class="degisiklik".*?</section>', ana, re.S)
    liste, tarih = [], ""
    for h4, tur, metin in re.findall(r'<h4>(.*?)</h4>|<p><span class="dg-tur[^"]*">(.*?)</span> (.*?)</p>', kutu.group(0) if kutu else ""):
        if h4:
            tarih = html.unescape(h4)
        else:
            liste.append({"tarih": tarih, "tur": html.unescape(tur), "metin": html.unescape(metin)})
    return liste


if os.path.exists("veri.json"):
    veri = json.load(open("veri.json", encoding="utf-8"))
else:
    veri = json.loads(parca(ana, r"\n    const DATA = (.*?);\n"))
if "updates" not in veri:
    veri["updates"] = son_degisiklikler()
# Gözetmen izin günleri (proctorAvailability) ana sitede yoksa v2'deki korunur
if "proctorAvailability" not in veri and os.path.exists("v2/veri.json"):
    eski = json.load(open("v2/veri.json", encoding="utf-8"))
    if "proctorAvailability" in eski:
        veri["proctorAvailability"] = eski["proctorAvailability"]

open("v2/veri.json", "w", encoding="utf-8", newline="\n").write(json.dumps(veri, ensure_ascii=False, indent=1) + "\n")

desen = r'panel/\?v=\d+"'
v2 = v2.replace(parca(v2, desen), parca(ana, desen))
open("v2/index.html", "w", encoding="utf-8", newline="\n").write(v2)
print("v2 eşitlendi:", len(veri["exams"]), "sınav,", len(veri["updates"]), "değişiklik notu")
