# Modul 5: Belirsizlik Altinda Triyaj ve Bulanik Mantik Denetleyicisi
# Sorumlu: Rol 9 (Bulanik Denetim & Matematiksel Modelleme)

from src.veri_yapilari import BulanikSonuc


def ucgen_uyelik(x, a, b, c):
    # TODO (Rol 9): Ucgen uyelik fonksiyonu formulunu yaz.
    return 0.0


def yamuk_uyelik(x, a, b, c, d):
    # TODO (Rol 9): Yamuk uyelik fonksiyonu formulunu yaz.
    return 0.0


def bulanik_triyaj_hesapla(ates, nabiz, agri_seviyesi):
    # TODO (Rol 9):
    # 1) Bulaniklastirma (Fuzzification): ates, nabiz, agri icin uyelik degerleri
    # 2) Mamdani min-max kural cikarimi
    # 3) Durulastirma (Centroid / Agirlik Merkezi) ile 0-100 arasi aciliyet skoru
    return BulanikSonuc(
        aciliyet_skoru=75.0,
        risk_seviyesi="Yuksek (Taslak)",
        uyelik_degerleri={},
    )
