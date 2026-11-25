# Modul 2: Hastane Yerleskesi Durum Uzayi Grafi
# Sorumlu: Rol 2 (Ajan & Durum Uzayi Modelleme Uzmani)


class HastaneGrafi:
    def __init__(self):
        # komsular ornek yapisi: {"Acil_Giris": [("Koridor_A", 5), ("Triyaj", 2)]}
        self.komsular = {}
        # koordinatlar sezgisel fonksiyon (Manhattan / Kus Ucusu) icin: {"Acil_Giris": (0, 0)}
        self.koordinatlar = {}

    def dugum_ekle(self, ad, x, y):
        if ad not in self.komsular:
            self.komsular[ad] = []
        self.koordinatlar[ad] = (x, y)

    def kenar_ekle(self, kaynak, hedef, maliyet, cift_yonlu=True):
        self.komsular[kaynak].append((hedef, maliyet))
        if cift_yonlu:
            self.komsular[hedef].append((kaynak, maliyet))


def hastane_grafini_olustur():
    # TODO (Rol 2): Gercek hastane yerleskesini (katlar, koridorlar, bloklar, birimler)
    # detayli sekilde ekle. Dugum isimlerini Rol 7 ile ortak belirle.
    graf = HastaneGrafi()

    # Baslangic icin ornek taslak dugumler
    graf.dugum_ekle("Acil_Giris", 0, 0)
    graf.dugum_ekle("Koridor_A", 2, 1)
    graf.dugum_ekle("Kardiyoloji", 5, 2)
    graf.dugum_ekle("Yogun_Bakim", 6, 4)
    graf.dugum_ekle("Ameliyathane", 8, 3)

    graf.kenar_ekle("Acil_Giris", "Koridor_A", 3)
    graf.kenar_ekle("Koridor_A", "Kardiyoloji", 4)
    graf.kenar_ekle("Koridor_A", "Yogun_Bakim", 6)
    graf.kenar_ekle("Kardiyoloji", "Ameliyathane", 5)
    graf.kenar_ekle("Yogun_Bakim", "Ameliyathane", 2)

    return graf
