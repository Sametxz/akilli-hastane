# Moduller arasi veri akisini yoneten ana koordinator (Rol 1)

from src.modul1_ajan_peas.peas_analizi import peas_tablosunu_getir, ortam_ozelliklerini_getir
from src.modul2_arama.graf import hastane_grafini_olustur
from src.modul2_arama.bilgisiz_arama import bfs_ara, dfs_ara, ucs_ara
from src.modul2_arama.bilgili_arama import greedy_ara, a_star_ara
from src.modul3_minimax.oyun_agaci import minimax_karar_ver
from src.modul3_minimax.alfa_beta import alfabeta_karar_ver
from src.modul4_kural_tabanli.bilgi_tabani import kurallari_getir
from src.modul4_kural_tabanli.cikarim_motoru import ileri_zincirleme_calistir
from src.modul5_bulanik.bulanik_triyaj import bulanik_triyaj_hesapla


class SistemKoordinatoru:
    def __init__(self):
        # Hastane grafi ve kural tabani sistem acilirken hazirlanir
        self.graf = hastane_grafini_olustur()
        self.kurallar = kurallari_getir()
        self.peas = peas_tablosunu_getir()
        self.ortam = ortam_ozelliklerini_getir()

    def acil_vaka_isle(self, hasta, kaynak_durumu, derinlik=3):
        """
        Bir hasta geldiginde tum modulleri sirasiyla calistirir
        ve tum ciktilari tek bir sozluk olarak dondurur.
        """
        # 1. Adim: Bulanik mantik ile aciliyet skoru hesapla (Modul 5)
        bulanik_sonuc = bulanik_triyaj_hesapla(
            hasta.ates,
            hasta.nabiz,
            hasta.agri_seviyesi,
        )

        # 2. Adim: Kural tabanli sistem ile on tani ve hedef birim belirle (Modul 4)
        cikarim_sonucu = ileri_zincirleme_calistir(hasta, bulanik_sonuc, self.kurallar)

        # 3. Adim: Kritik kaynak dagitimi icin Minimax ve Alfa-Beta karsilastir (Modul 3)
        minimax_sonuc = minimax_karar_ver(kaynak_durumu, bulanik_sonuc.aciliyet_skoru, derinlik)
        kaynak_karari = alfabeta_karar_ver(
            kaynak_durumu,
            bulanik_sonuc.aciliyet_skoru,
            derinlik,
            minimax_dugum_sayisi=minimax_sonuc.minimax_dugum_sayisi,
        )

        # 4. Adim: Hastanin bulundugu yerden hedef birime tum arama algoritmalarini calistir (Modul 2)
        baslangic = hasta.bulundugu_konum
        hedef = cikarim_sonucu.hedef_birim

        arama_sonuclari = [
            bfs_ara(self.graf, baslangic, hedef),
            dfs_ara(self.graf, baslangic, hedef),
            ucs_ara(self.graf, baslangic, hedef),
            greedy_ara(self.graf, baslangic, hedef),
            a_star_ara(self.graf, baslangic, hedef),
        ]

        return {
            "hasta": hasta,
            "bulanik_sonuc": bulanik_sonuc,
            "cikarim_sonucu": cikarim_sonucu,
            "kaynak_karari": kaynak_karari,
            "arama_sonuclari": arama_sonuclari,
        }
