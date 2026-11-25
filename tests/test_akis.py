# Moduller arasi veri akisinin bozulmadigini kontrol eden basit test (Rol 1 & Rol 10)

import os
import sys

# Proje ana klasorunu Python yoluna ekle
PROJE_YOLU = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJE_YOLU not in sys.path:
    sys.path.insert(0, PROJE_YOLU)

from src.veri_yapilari import Hasta, KaynakDurumu
from src.sistem_koordinatoru import SistemKoordinatoru


def test_temel_akis():
    koordinator = SistemKoordinatoru()
    hasta = Hasta(
        ad="Test Hasta",
        yas=55,
        ates=38.2,
        nabiz=110,
        tansiyon_buyuk=145,
        tansiyon_kucuk=90,
        agri_seviyesi=7,
        gogus_agrisi=True,
        bulundugu_konum="Acil_Giris",
    )
    kaynaklar = KaynakDurumu(1, 1, 1)

    sonuc = koordinator.acil_vaka_isle(hasta, kaynaklar)

    assert sonuc["bulanik_sonuc"] is not None, "Bulanik sonuc bos dondu"
    assert sonuc["cikarim_sonucu"].hedef_birim in koordinator.graf.komsular, (
        "Hedef birim graf icinde bulunamadi!"
    )
    assert sonuc["kaynak_karari"] is not None, "Kaynak karari bos dondu"
    assert len(sonuc["arama_sonuclari"]) == 5, "5 arama algoritmasi sonucu donmeli"

    print("Basarili: Moduller arasi temel veri akisi sorunsuz calisti.")


if __name__ == "__main__":
    test_temel_akis()
