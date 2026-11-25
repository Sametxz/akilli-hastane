# Modul 1: Ajan Mimarisi, PEAS Analizi ve Ortam Karakterizasyonu
# Sorumlu: Rol 2 (Ajan & Durum Uzayi Modelleme Uzmani)
#
# Sistemde iki ajan var:
# 1) Acil Mudahale Koordinatoru: hastayi degerlendirir, birim ve kaynak karari verir.
#    Modul 3'teki kaynak oyununda acil vaka tarafini (MAX) temsil eder.
# 2) Otonom Sedye Robotu: hastayi graf uzerinde hedef birime tasir (Modul 2 rotasi).
# Rakip taraf "Planli Operasyon Yonetimi" (MIN) ayni kaynaklar icin rekabet eder.


def peas_tablosunu_getir():
    return {
        "Acil Mudahale Koordinatoru": {
            "Performance (Performans)": (
                "Hastanin dogru birime yonlendirilmesi, kritik hastanin bekleme suresinin "
                "kisa olmasi, yogun bakim / ameliyathane gibi sinirli kaynaklarin dogru "
                "dagitilmasi, hayatta kalma orani"
            ),
            "Environment (Ortam)": (
                "Acil servis ve hastane yerleskesi, hastalar, saglik personeli, "
                "yogun bakim yataklari, ameliyathaneler, planli operasyon listesi"
            ),
            "Actuators (Eyleyiciler)": (
                "Ekran / bildirim (triyaj seviyesi, on tani ve karar aciklamasi gosterme), "
                "sedye robotuna hedef birim ve rota komutu gonderme, "
                "hastane sistemine yatak / ameliyathane rezervasyon kaydi yazma"
            ),
            "Sensors (Algilayicilar)": (
                "Hasta bilgi girisi (yas, ates, nabiz, tansiyon, agri seviyesi, gogus agrisi), "
                "hastanin bulundugu konum, bos yogun bakim yatagi / ameliyathane / "
                "hazir cerrahi ekip bilgisi"
            ),
        },
        "Otonom Sedye Robotu": {
            "Performance (Performans)": (
                "Hedefe en kisa surede ve en dusuk maliyetle ulasmak, carpisma olmamasi, "
                "hastanin guvenli tasinmasi"
            ),
            "Environment (Ortam)": (
                "Hastane koridorlari, katlar, asansorler, birim kapilari, "
                "koridordaki insanlar ve diger robotlar"
            ),
            "Actuators (Eyleyiciler)": (
                "Tekerlek motorlari (ileri gitme, donme, durma), asansor cagirma, "
                "sesli / isikli uyari"
            ),
            "Sensors (Algilayicilar)": (
                "Konum bilgisi (bulundugu dugum), mesafe sensoru, kamera, "
                "koordinatorden gelen hedef birim bilgisi"
            ),
        },
    }


def ajan_tiplerini_getir():
    return {
        "Acil Mudahale Koordinatoru": (
            "Fayda tabanli ajan. Kural tabani (Modul 4) ve bulanik triyaj (Modul 5) ile "
            "hastayi degerlendirir, kaynak dagitiminda Minimax (Modul 3) ile en yuksek "
            "fayda skorunu veren karari secer."
        ),
        "Otonom Sedye Robotu": (
            "Hedef tabanli ajan. Hedefi koordinatorden gelen birimdir, oraya ulasmak icin "
            "graf uzerinde arama (Modul 2) yaparak bir yol plani cikarir."
        ),
    }


def ortam_ozelliklerini_getir():
    # Her ozellikte once gercek hastane ortami, sonra projedeki modelin yaptigi
    # basitlestirme yazildi.
    return {
        "Gozlemlenebilirlik": (
            "Kismi gozlemlenebilir. Ajan hastanin sadece olculen degerlerini gorur, "
            "hastaligin kesin durumunu bilemez. Robot da koridorun tamamini goremez. "
            "Modelde: rota planlanirken graf ve kenar maliyetlerinin tamami bilindigi kabul edilir."
        ),
        "Deterministik / Stokastik": (
            "Stokastik. Hastanin durumu aniden kotulesebilir, yeni hasta gelebilir, "
            "koridor kapanabilir. Ayni eylem her zaman ayni sonucu vermez. "
            "Modelde: arama ve Minimax deterministik kabul edilir (her hareketin sonucu bellidir). "
            "Belirsizlik olcum tarafinda bulanik mantik (Modul 5) ile ele alinir."
        ),
        "Epizodik / Ardisik": (
            "Ardisik. Bir hastaya yatak ayirmak sonraki hasta icin kalan kaynagi "
            "etkiler. Robotun her adimi bir sonraki konumunu belirler. "
            "Modelde: her hasta vakasi ayri islenir, ama vaka icinde rota ve kaynak "
            "kararlari ardisik adimlardan olusur."
        ),
        "Statik / Dinamik": (
            "Dinamik. Ajan karar verirken ortam degismeye devam eder "
            "(yeni hastalar gelir, yataklar dolar, koridorlar yogunlasir). "
            "Modelde: karar verilen an icin ortamin sabit kaldigi kabul edilir; "
            "ortam degisirse arama yeniden calistirilir."
        ),
        "Ayrik / Surekli": (
            "Graf uzerinde rota bulma acisindan ayrik (sonlu sayida dugum ve hareket). "
            "Ates, nabiz gibi olcumler ise surekli degerlerdir."
        ),
        "Tek / Coklu Ajan": (
            "Coklu ajan. Koordinator ile sedye robotu ayni amaca hizmet eder (isbirlikci). "
            "Koordinatorun temsil ettigi acil vaka tarafi (MAX) ile Planli Operasyon "
            "Yonetimi (MIN) ayni yogun bakim / ameliyathane kaynaklari icin rekabet eder "
            "(rekabetci, Modul 3)."
        ),
    }


def peas_tablosunu_yazdir():
    # PEAS tablosunu konsola tablo seklinde yazar (rapor ve demo icin)
    tablo = peas_tablosunu_getir()
    tipler = ajan_tiplerini_getir()
    for ajan, bilesenler in tablo.items():
        print("=" * 70)
        print(ajan + " - " + tipler[ajan].split(".")[0])
        print("=" * 70)
        for baslik, aciklama in bilesenler.items():
            print("%-26s | %s" % (baslik, aciklama))
        print()
