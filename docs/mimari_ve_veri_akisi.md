# Sistem Mimarisi ve Moduller Arasi Veri Akisi

Bu dokuman, 5 yapay zeka modulunun birbirine nasil baglanacagini ve ortak fonksiyon giris-cikis formatlarini tanimlar. Her ekip uyesi kendi modulunu yazarken buradaki veri tiplerine sadik kalmalidir.

## 1. Genel Veri Akisi

Acil servise yeni bir hasta geldiginde sistem asagidaki sirayla calisir:

```text
[1. Hasta Girisi (GUI veya Konsol)]
        |
        v
[Modül 5: Bulanik Triyaj (Rol 9)]
  Girdi : ates, nabiz, agri_seviyesi
  Cikti : BulanikSonuc (aciliyet_skoru: 0-100, risk_seviyesi)
        |
        v
[Modül 4: Kural Tabanli Cikarim (Rol 7 & Rol 8)]
  Girdi : Hasta bilgileri + BulanikSonuc
  Cikti : CikarimSonucu (on_tani, hedef_birim, aciklama_adimlari)
        |
        v
[Modül 3: Minimax & Alfa-Beta Kaynak Dagitimi (Rol 5 & Rol 6)]
  Girdi : Mevcut hastane kaynaklari + Acil vaka puani + Planli operasyon puani
  Cikti : KaynakKarari (secilen_karar, minimax_dugum, alfabeta_dugum, tasarruf_orani)
        |
        v
[Modül 2: Navigasyon Arama Motoru (Rol 2, Rol 3 & Rol 4)]
  Girdi : Hastane grafi, baslangic noktasi, hedef_birim
  Cikti : AramaSonucu listesi (BFS, DFS/IDS, UCS, Greedy, A* karsilastirmasi)
        |
        v
[Arayuz & Raporlama (Rol 10)]
  Tum sonuclar, karsilastirma tablolari ve aciklamalar ekranda gosterilir.
```

> Not: Modul 1 (PEAS Analizi ve Ortam Karakterizasyonu - Rol 2) sistemin genel ajan tanimini ve ortam ozelliklerini saglar, arayuzde bilgi ekrani olarak ve teknik raporda sunulur.

## 2. Ortak Veri Yapilari (`src/veri_yapilari.py`)

Tum moduller asagidaki sade Python siniflarini kullanir:

- **`Hasta`**: `ad`, `yas`, `ates`, `nabiz`, `tansiyon_buyuk`, `tansiyon_kucuk`, `agri_seviyesi`, `gogus_agrisi` (True/False), `bulundugu_konum`.
- **`BulanikSonuc`**: `aciliyet_skoru` (float, 0-100), `risk_seviyesi` (str: `"Dusuk"`, `"Orta"`, `"Yuksek"`, `"Kritik"`), `uyelik_degerleri` (dict).
- **`CikarimSonucu`**: `on_tani` (str), `hedef_birim` (str, graftaki dugum adiyla ayni olmali), `tetiklenen_kurallar` (list), `aciklama_adimlari` (list).
- **`KaynakKarari`**: `secilen_aksiyon` (str), `en_iyi_skor` (float), `minimax_dugum_sayisi` (int), `alfabeta_dugum_sayisi` (int), `budanan_dugum_sayisi` (int), `tasarruf_yuzdesi` (float).
- **`AramaSonucu`**: `algoritma_adi` (str), `yol` (list), `toplam_maliyet` (float), `genisletilen_dugum` (int), `sure_ms` (float), `open_listesi_son` (list), `closed_listesi_son` (list).

## 3. Kritik Uyum Kurallari

1. **Dugum Isimleri Uyumu (Rol 2, Rol 7, Rol 10):**
   Rol 7'nin kural tabaninda dondurdugu `hedef_birim` degeri (ornek: `"Kardiyoloji"`, `"Yogun_Bakim"`, `"Ameliyathane"`, `"Acil_Musahede"`), Rol 2'nin `graf.py` dosyasindaki dugum isimleriyle birebir ayni olmalidir.
2. **Ayni Oyun Agaci Kullanimi (Rol 5 & Rol 6):**
   Minimax ve Alfa-Beta budama karsilastirmasinin dogru cikmasi icin Rol 6, Rol 5'in kurdugu ayni oyun agaci/durum yapisi uzerinde calismalidir.
3. **Sifirdan Kodlama Kurali:**
   Hicbir arama, minimax, kural motoru veya bulanik mantik algoritmasinda hazir yapay zeka/graf kutuphanesi (`networkx`, `scikit-fuzzy` vb.) kullanilmayacaktir. Sadece Python standart kutuphaneleri kullanilacaktir.
