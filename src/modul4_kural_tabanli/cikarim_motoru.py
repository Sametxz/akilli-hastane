# Modul 4: Ileri/Geri Zincirleme Cikarim Motoru ve Aciklama Mekanizmasi
# Sorumlu: Rol 8 (Cikarim Motoru & Aciklama Modulu Sorumlusu)

from src.veri_yapilari import CikarimSonucu


def ileri_zincirleme_calistir(hasta, bulanik_sonuc, kurallar):
    # TODO (Rol 8): Hasta olgularini (facts) kullanarak Modus Ponens mantigiyla
    # ileriye dogru zincirleme (Forward Chaining) calistir.
    # Ayni anda birden fazla kural tetiklenirse Rol 7'nin oncelik stratejisine gore sec.
    # Ayrica "Bu karar neden verildi?" sorusuna adim adim aciklama_adimlari uret.
    return CikarimSonucu(
        on_tani="Taslak On Tani",
        hedef_birim="Kardiyoloji",
        tetiklenen_kurallar=["K1"],
        aciklama_adimlari=[
            "Taslak aciklama: Gercek kural zinciri Rol 8 tarafindan eklenecek."
        ],
    )
