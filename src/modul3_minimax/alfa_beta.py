# Modul 3: Alfa-Beta Budama, Statik Degerlendirme ve Performans Analizi
# Sorumlu: Rol 6 (Alfa-Beta Budama & Analiz Sorumlusu)

from src.veri_yapilari import KaynakKarari


def statik_degerlendir(durum, derinlik):
    # TODO (Rol 6): Agacin derinlik sinirina bagli statik degerlendirme fonksiyonunu yaz.
    return 0.0


def alfabeta_karar_ver(kaynak_durumu, acil_vaka_skoru, derinlik=3, minimax_dugum_sayisi=0):
    # TODO (Rol 6): Rol 5'in kurdugu ayni oyun agaci uzerinde Alfa-Beta budama calistir.
    # Gezilen dugum sayisini say ve Minimax'a gore kac dugum budandigini KaynakKarari ile dondur.
    return KaynakKarari(
        secilen_aksiyon="Taslak - Acil vakaya yogun bakim tahsis et",
        en_iyi_skor=0.0,
        minimax_dugum_sayisi=minimax_dugum_sayisi,
        alfabeta_dugum_sayisi=0,
    )
