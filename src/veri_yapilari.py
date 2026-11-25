# Tum modullerin ortak kullandigi veri siniflari (Rol 1)
# Her modul ayni siniflari kullanir ki entegrasyonda veri uyusmazligi olmasin.


class Hasta:
    def __init__(
        self,
        ad,
        yas,
        ates,
        nabiz,
        tansiyon_buyuk,
        tansiyon_kucuk,
        agri_seviyesi,
        gogus_agrisi=False,
        bulundugu_konum="Acil_Giris",
    ):
        self.ad = ad
        self.yas = yas
        self.ates = ates
        self.nabiz = nabiz
        self.tansiyon_buyuk = tansiyon_buyuk
        self.tansiyon_kucuk = tansiyon_kucuk
        self.agri_seviyesi = agri_seviyesi  # 0 ile 10 arasi
        self.gogus_agrisi = gogus_agrisi
        self.bulundugu_konum = bulundugu_konum


class BulanikSonuc:
    def __init__(self, aciliyet_skoru, risk_seviyesi, uyelik_degerleri=None):
        self.aciliyet_skoru = aciliyet_skoru  # 0-100 arasi durulastirilmis sonuc
        self.risk_seviyesi = risk_seviyesi    # Dusuk, Orta, Yuksek, Kritik
        if uyelik_degerleri is None:
            self.uyelik_degerleri = {}
        else:
            self.uyelik_degerleri = uyelik_degerleri


class CikarimSonucu:
    def __init__(self, on_tani, hedef_birim, tetiklenen_kurallar=None, aciklama_adimlari=None):
        self.on_tani = on_tani
        self.hedef_birim = hedef_birim  # Graftaki dugum adi ile ayni olmali
        self.tetiklenen_kurallar = tetiklenen_kurallar if tetiklenen_kurallar is not None else []
        self.aciklama_adimlari = aciklama_adimlari if aciklama_adimlari is not None else []


class KaynakDurumu:
    def __init__(self, bos_yogun_bakim, bos_ameliyathane, hazir_cerrahi_ekip):
        self.bos_yogun_bakim = bos_yogun_bakim
        self.bos_ameliyathane = bos_ameliyathane
        self.hazir_cerrahi_ekip = hazir_cerrahi_ekip


class KaynakKarari:
    def __init__(
        self,
        secilen_aksiyon,
        en_iyi_skor,
        minimax_dugum_sayisi=0,
        alfabeta_dugum_sayisi=0,
    ):
        self.secilen_aksiyon = secilen_aksiyon
        self.en_iyi_skor = en_iyi_skor
        self.minimax_dugum_sayisi = minimax_dugum_sayisi
        self.alfabeta_dugum_sayisi = alfabeta_dugum_sayisi
        self.budanan_dugum_sayisi = max(0, minimax_dugum_sayisi - alfabeta_dugum_sayisi)
        if minimax_dugum_sayisi > 0:
            self.tasarruf_yuzdesi = (self.budanan_dugum_sayisi / minimax_dugum_sayisi) * 100
        else:
            self.tasarruf_yuzdesi = 0.0


class AramaSonucu:
    def __init__(
        self,
        algoritma_adi,
        yol,
        toplam_maliyet,
        genisletilen_dugum,
        sure_ms,
        open_listesi_son=None,
        closed_listesi_son=None,
    ):
        self.algoritma_adi = algoritma_adi
        self.yol = yol
        self.toplam_maliyet = toplam_maliyet
        self.genisletilen_dugum = genisletilen_dugum
        self.sure_ms = sure_ms
        self.open_listesi_son = open_listesi_son if open_listesi_son is not None else []
        self.closed_listesi_son = closed_listesi_son if closed_listesi_son is not None else []
