# Modul 3: Rekabetci Arama, Oyun Agaci ve Minimax
# Sorumlu: Rol 5 (Rekabetci Arama & Minimax Sorumlusu)

from src.veri_yapilari import KaynakKarari


def oyun_agaci_olustur(kaynak_durumu, acil_vaka_skoru, derinlik=3):
    # TODO (Rol 5): Acil Vaka Triyaj Masasi (MAX) ile Planli Operasyon Yonetimi (MIN)
    # arasindaki kaynak paylasim oyun agacini olustur.
    # Rol 6 bu ayni agac yapisini Alfa-Beta budama icin kullanacak.
    return {}


def minimax_karar_ver(kaynak_durumu, acil_vaka_skoru, derinlik=3):
    # TODO (Rol 5): Minimax algoritmasini sifirdan yaz ve gezilen dugum sayisini say.
    return KaynakKarari(
        secilen_aksiyon="Taslak - Acil vakaya yogun bakim tahsis et",
        en_iyi_skor=0.0,
        minimax_dugum_sayisi=0,
        alfabeta_dugum_sayisi=0,
    )
