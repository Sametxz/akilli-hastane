# Projenin ana baslangic dosyasi (Rol 1)

from src.veri_yapilari import Hasta, KaynakDurumu
from src.sistem_koordinatoru import SistemKoordinatoru
from src.arayuz.gui import arayuzu_baslat


def ornek_konsol_calistir():
    koordinator = SistemKoordinatoru()

    ornek_hasta = Hasta(
        ad="Ahmet Yilmaz",
        yas=62,
        ates=38.6,
        nabiz=118,
        tansiyon_buyuk=150,
        tansiyon_kucuk=95,
        agri_seviyesi=8,
        gogus_agrisi=True,
        bulundugu_konum="Acil_Giris",
    )

    kaynaklar = KaynakDurumu(
        bos_yogun_bakim=1,
        bos_ameliyathane=1,
        hazir_cerrahi_ekip=1,
    )

    sonuc = koordinator.acil_vaka_isle(ornek_hasta, kaynaklar)

    print("=== AKILLI HASTANE SISTEMI - ORNEK AKIS ===")
    print("Hasta:", sonuc["hasta"].ad)
    print(
        "Bulanik Triyaj Skoru:",
        sonuc["bulanik_sonuc"].aciliyet_skoru,
        "- Risk:",
        sonuc["bulanik_sonuc"].risk_seviyesi,
    )
    print("On Tani:", sonuc["cikarim_sonucu"].on_tani)
    print("Hedef Birim:", sonuc["cikarim_sonucu"].hedef_birim)
    print("Kaynak Karari:", sonuc["kaynak_karari"].secilen_aksiyon)
    print(
        f"Budama Tasarrufu: %{sonuc['kaynak_karari'].tasarruf_yuzdesi:.2f} "
        f"(Minimax: {sonuc['kaynak_karari'].minimax_dugum_sayisi}, "
        f"Alfa-Beta: {sonuc['kaynak_karari'].alfabeta_dugum_sayisi})"
    )
    print("\n--- Arama Algoritmalari Karsilastirmasi ---")
    for arama in sonuc["arama_sonuclari"]:
        yol_metni = " -> ".join(arama.yol)
        print(
            f"{arama.algoritma_adi} | Yol: {yol_metni} | "
            f"Maliyet: {arama.toplam_maliyet:.1f} | "
            f"Genisletilen: {arama.genisletilen_dugum} | "
            f"Sure: {arama.sure_ms:.3f} ms"
        )


if __name__ == "__main__":
    print("1 - Konsol ornek akisini calistir")
    print("2 - Arayuzu (GUI) baslat")
    secim = input("Seciminiz (varsayilan 1): ").strip()

    if secim == "2":
        arayuzu_baslat()
    else:
        ornek_konsol_calistir()
