# Modul 4: Tibbi Bilgi Tabani, IF-THEN Kurallari ve Cakisma Oncelikleri
# Sorumlu: Rol 7 (Mantiksal Bilgi Tabani Muhendisi)


def kurallari_getir():
    # TODO (Rol 7): Tibbi olgulara gore IF-THEN kurallarini ve cakisma cozumu icin
    # oncelik degerlerini (yuksek sayi = yuksek oncelik) ekle.
    # hedef_birim degerleri Rol 2'nin graf.py dugum isimleriyle ayni olmali.
    ornek_kurallar = [
        {
            "id": "K1",
            "oncelik": 100,
            "aciklama": "Yas > 50 ve gogus agrisi varsa yuksek kardiyak risk",
            "on_tani": "Akut Koroner Sendrom Suphesi (Taslak)",
            "hedef_birim": "Kardiyoloji",
        }
    ]
    return ornek_kurallar
