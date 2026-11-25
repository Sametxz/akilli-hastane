# Modul 2: Hastane Yerleskesi Durum Uzayi Grafi
# Sorumlu: Rol 2 (Ajan & Durum Uzayi Modelleme Uzmani)
#
# Durum uzayi: G = (V, E)
#   V = hastanedeki konumlar (birimler, koridorlar, asansorler)
#   E = iki konum arasindaki yol, agirligi = yol maliyeti
#
# Birim: 1 birim = 10 metre yurume mesafesi. Koordinatlar da ayni birimde.
# Asansor gibi yuruyus olmayan gecislerde maliyet "esdeger yurume mesafesi" olarak verildi
# (ornek: asansor bekleme + gecis suresi ~ 50 metre yurumeye esit -> 5).
#
# Kural: her kenarin maliyeti, iki ucunun Manhattan mesafesinden kucuk olamaz.
#   c(n, n') >= Manhattan(n, n') >= Kus Ucusu(n, n')
# Sonuc:
#   - Kabul edilebilir (admissible): h(n) <= n'den hedefe gercek maliyet.
#   - Tutarli (consistent): h(n) <= c(n, n') + h(n')  (ucgen esitsizliginden).
#     Tutarlilik sayesinde A*, CLOSED listesine aldigi dugumu tekrar acmak zorunda kalmaz
#     ve en kisa yolu bulmayi garanti eder.
# Sezgiseller 2 boyutludur (kat bilgisini kullanmaz). Asansorun iki ucu ayni (x, y)
# noktasinda oldugu icin aralarindaki h = 0 olur, bu da kurali bozmaz.


class HastaneGrafi:
    def __init__(self):
        # komsular ornek yapisi: {"Acil_Giris": [("Triyaj", 2), ("Bahce_Yolu", 15)]}
        self.komsular = {}
        # koordinatlar sezgisel fonksiyon (Manhattan / Kus Ucusu) icin: {"Acil_Giris": (2, 0)}
        self.koordinatlar = {}
        # dugumun bulundugu kat: {"Ameliyathane": 1}
        self.katlar = {}

    def dugum_ekle(self, ad, x, y, kat=0):
        # Ayni isimle ikinci kez eklenirse koordinat sessizce degismesin diye hata verir
        if ad in self.komsular:
            raise ValueError("Bu dugum zaten var: " + ad)
        self.komsular[ad] = []
        self.koordinatlar[ad] = (x, y)
        self.katlar[ad] = kat

    def kenar_ekle(self, kaynak, hedef, maliyet, cift_yonlu=True):
        if kaynak not in self.komsular or hedef not in self.komsular:
            raise ValueError("Kenar eklenmeden once dugumler eklenmeli: " + kaynak + " - " + hedef)
        if kaynak == hedef:
            raise ValueError("Dugum kendisine baglanamaz: " + kaynak)
        if maliyet <= 0:
            raise ValueError("Kenar maliyeti pozitif olmali: " + kaynak + " - " + hedef)
        for komsu, _ in self.komsular[kaynak]:
            if komsu == hedef:
                raise ValueError("Bu kenar zaten var: " + kaynak + " - " + hedef)
        self.komsular[kaynak].append((hedef, maliyet))
        if cift_yonlu:
            self.komsular[hedef].append((kaynak, maliyet))

    def komsulari_getir(self, dugum):
        # Listenin kopyasini dondurur; arama algoritmasi listeyi degistirse bile graf bozulmaz
        if dugum not in self.komsular:
            raise ValueError("Grafta boyle bir dugum yok: " + str(dugum))
        return list(self.komsular[dugum])

    def maliyet_kuralini_kontrol_et(self):
        # Manhattan mesafesinden ucuz olan kenarlari bulur (bos liste = kural saglaniyor)
        hatali_kenarlar = []
        bakilan_kenarlar = set()
        for dugum in self.komsular:
            x1, y1 = self.koordinatlar[dugum]
            for komsu, maliyet in self.komsular[dugum]:
                # Cift yonlu kenari (A-B ve B-A) bir kere kontrol et
                if (komsu, dugum) in bakilan_kenarlar:
                    continue
                bakilan_kenarlar.add((dugum, komsu))
                x2, y2 = self.koordinatlar[komsu]
                manhattan = abs(x1 - x2) + abs(y1 - y2)
                if maliyet < manhattan:
                    hatali_kenarlar.append((dugum, komsu, maliyet, manhattan))
        return hatali_kenarlar


def hastane_grafini_olustur():
    graf = HastaneGrafi()

    # ---------------- ZEMIN KAT (kat 0) ----------------
    # A Blok: Acil servis
    graf.dugum_ekle("Ambulans_Girisi", 0, 0)
    graf.dugum_ekle("Acil_Giris", 2, 0)
    graf.dugum_ekle("Triyaj", 4, 0)
    graf.dugum_ekle("Resusitasyon", 4, 2)
    graf.dugum_ekle("Acil_Musahede", 6, 0)
    graf.dugum_ekle("Acil_Koridoru", 6, 2)
    graf.dugum_ekle("Laboratuvar", 6, 4)
    graf.dugum_ekle("Radyoloji", 8, 2)

    # B Blok: Poliklinikler
    graf.dugum_ekle("Ana_Koridor", 10, 2)
    graf.dugum_ekle("Eczane", 10, 0)
    graf.dugum_ekle("Kardiyoloji", 12, 0)
    graf.dugum_ekle("Noroloji", 12, 4)
    graf.dugum_ekle("Poliklinik_Koridoru", 14, 2)
    graf.dugum_ekle("Ortopedi", 14, 4)
    graf.dugum_ekle("Asansor_Zemin", 16, 2)  # B ve C blok arasindaki ana asansor

    # Dis alan ve C Blok girisi
    graf.dugum_ekle("Bahce_Yolu", 8, 8)
    graf.dugum_ekle("C_Blok_Girisi", 16, 8)
    graf.dugum_ekle("Servis_Asansoru_Zemin", 16, 6)

    # ---------------- 1. KAT (kat 1) - C Blok: Cerrahi ve yogun bakim ----------------
    graf.dugum_ekle("Asansor_Kat1", 16, 2, kat=1)
    graf.dugum_ekle("Servis_Asansoru_Kat1", 16, 6, kat=1)
    graf.dugum_ekle("Cerrahi_Koridoru", 18, 4, kat=1)
    graf.dugum_ekle("Ameliyathane", 20, 2, kat=1)
    graf.dugum_ekle("Yogun_Bakim", 20, 6, kat=1)
    graf.dugum_ekle("Koroner_Yogun_Bakim", 18, 0, kat=1)

    # ---------------- KENARLAR (zemin kat) ----------------
    graf.kenar_ekle("Ambulans_Girisi", "Acil_Giris", 2)
    graf.kenar_ekle("Acil_Giris", "Triyaj", 2)
    graf.kenar_ekle("Triyaj", "Resusitasyon", 2)
    graf.kenar_ekle("Triyaj", "Acil_Musahede", 2)
    graf.kenar_ekle("Resusitasyon", "Acil_Koridoru", 2)
    graf.kenar_ekle("Acil_Musahede", "Acil_Koridoru", 2)
    graf.kenar_ekle("Acil_Koridoru", "Laboratuvar", 2)
    graf.kenar_ekle("Acil_Koridoru", "Radyoloji", 2)
    graf.kenar_ekle("Radyoloji", "Ana_Koridor", 2)
    graf.kenar_ekle("Laboratuvar", "Ana_Koridor", 6)

    graf.kenar_ekle("Ana_Koridor", "Eczane", 2)
    graf.kenar_ekle("Ana_Koridor", "Kardiyoloji", 4)
    graf.kenar_ekle("Eczane", "Kardiyoloji", 2)
    graf.kenar_ekle("Ana_Koridor", "Noroloji", 4)
    graf.kenar_ekle("Ana_Koridor", "Poliklinik_Koridoru", 4)
    graf.kenar_ekle("Kardiyoloji", "Poliklinik_Koridoru", 4)
    graf.kenar_ekle("Noroloji", "Ortopedi", 2)
    graf.kenar_ekle("Poliklinik_Koridoru", "Ortopedi", 2)
    graf.kenar_ekle("Poliklinik_Koridoru", "Asansor_Zemin", 2)
    graf.kenar_ekle("Ortopedi", "Servis_Asansoru_Zemin", 4)

    # Bahce yolu: az adimli ama uzun dis yol (BFS ile UCS farkini gostermek icin)
    graf.kenar_ekle("Acil_Giris", "Bahce_Yolu", 15)
    graf.kenar_ekle("Laboratuvar", "Bahce_Yolu", 7)
    graf.kenar_ekle("Bahce_Yolu", "C_Blok_Girisi", 9)
    graf.kenar_ekle("C_Blok_Girisi", "Servis_Asansoru_Zemin", 2)

    # ---------------- ASANSORLER (kat gecisi) ----------------
    # Koordinat ayni oldugu icin Manhattan = 0, maliyet = bekleme + gecis (esdeger yurume mesafesi)
    graf.kenar_ekle("Asansor_Zemin", "Asansor_Kat1", 5)
    graf.kenar_ekle("Servis_Asansoru_Zemin", "Servis_Asansoru_Kat1", 4)

    # ---------------- KENARLAR (1. kat) ----------------
    graf.kenar_ekle("Asansor_Kat1", "Cerrahi_Koridoru", 4)
    graf.kenar_ekle("Asansor_Kat1", "Koroner_Yogun_Bakim", 4)
    graf.kenar_ekle("Servis_Asansoru_Kat1", "Cerrahi_Koridoru", 4)
    graf.kenar_ekle("Servis_Asansoru_Kat1", "Yogun_Bakim", 4)
    graf.kenar_ekle("Cerrahi_Koridoru", "Ameliyathane", 4)
    graf.kenar_ekle("Cerrahi_Koridoru", "Yogun_Bakim", 4)
    graf.kenar_ekle("Cerrahi_Koridoru", "Koroner_Yogun_Bakim", 4)
    graf.kenar_ekle("Ameliyathane", "Yogun_Bakim", 4)

    # Maliyet kurali bozulursa A* garantisi kalkar, bu yuzden graf olusurken kontrol edilir
    hatalar = graf.maliyet_kuralini_kontrol_et()
    if hatalar:
        raise ValueError("Manhattan mesafesinden ucuz kenarlar var: " + str(hatalar))

    return graf
