# Proje Takvimi ve Ekip Ici Teslim Tarihleri (25 Kasim - 3 Aralik)

Toplam suremiz 8 gun oldugu icin birbirini bekleyen modullerin zamaninda bitmesi cok onemlidir. Asagidaki tarihler diger ekip arkadaslarinin kilitlenmemesi icin belirlenmistir.

## Faz 1: Altyapi ve Temel Veri Modelleri (25 - 27 Kasim)

| Rol | Gorev | Baslangic | Son Teslim (Deadline) | Kimi Etkiler? |
|---|---|---|---|---|
| **Rol 1** | GitHub repo kurulumu, klasor yapisi, `veri_yapilari.py` ve `sistem_koordinatoru.py` taslagi | 25 Kasim | **26 Kasim 12:00** | Tum ekip (Rol 2-10) |
| **Rol 2** | PEAS tablosu (`peas_analizi.py`) ve **Hastane Grafi (`graf.py`)** | 26 Kasim | **27 Kasim 18:00** | Rol 3, Rol 4, Rol 7 |
| **Rol 7** | Tibbi olgular, IF-THEN kurallari ve cakisma oncelikleri (`bilgi_tabani.py`) | 26 Kasim | **27 Kasim 18:00** | Rol 8 |

> **Onemli:** Rol 2 dugum isimlerini (ornek: `Acil_Giris`, `Ameliyathane`, `Yogun_Bakim`) 26 Kasim aksami grupta paylasmalidir ki Rol 7 kurallari buna gore yazabilsin.

## Faz 2: Cekirdek Algoritmalarin Kodlanmasi (27 - 30 Kasim)

| Rol | Gorev | Baslangic | Son Teslim (Deadline) | Kimi Etkiler? |
|---|---|---|---|---|
| **Rol 3** | BFS, DFS/IDS, UCS algoritmalari + OPEN/CLOSED ve metrikler | 27 Kasim | **29 Kasim 21:00** | Rol 1, Rol 10 |
| **Rol 4** | Greedy Best-First, A* ve Manhattan/SLD sezgisel fonksiyonlari | 27 Kasim | **29 Kasim 21:00** | Rol 1, Rol 10 |
| **Rol 5** | Kaynak paylasim oyun agaci ve Minimax algoritmasi | 27 Kasim | **29 Kasim 18:00** | Rol 6 (Agac yapisi 28 Kasim aksami hazir olmali) |
| **Rol 6** | Statik degerlendirme fonksiyonu, Alfa-Beta budama ve tasarruf analizi | 28 Kasim | **30 Kasim 18:00** | Rol 1, Rol 10 |
| **Rol 8** | Ileri/Geri zincirleme cikarim motoru ve adim adim aciklama mekanizmasi | 28 Kasim | **30 Kasim 18:00** | Rol 1, Rol 10 |
| **Rol 9** | Ucgen/Yamuk uyelik fonksiyonlari, Mamdani min-max ve Centroid | 27 Kasim | **30 Kasim 18:00** | Rol 1, Rol 10 |

## Faz 3: Entegrasyon, Arayuz ve Test (30 Kasim - 2 Aralik)

| Rol | Gorev | Baslangic | Son Teslim (Deadline) | Aciklama |
|---|---|---|---|---|
| **Rol 10** | Arayuz (GUI) taslagi | 28 Kasim | 30 Kasim | Moduller bitmeden taslak arayuz hazirlanir |
| **Rol 1** | Pull Request incelemeleri ve `sistem_koordinatoru.py` gercek entegrasyonu | 30 Kasim | **1 Aralik 18:00** | Tum moduller `main` dalinda birlestirilir |
| **Rol 10** | Gercek modullerin GUI'ye baglanmasi, kiyaslama tablolari ve senaryo testleri | 1 Aralik | **2 Aralik 15:00** | Canli demo akisi sorunsuz calisir hale getirilir |

## Faz 4: Rapor, Sunum ve Savunma Provasi (2 - 3 Aralik)

- **2 Aralik 15:00 - 22:00:** Herkes kendi bolumunun teknik rapor kismini yazar, Rol 1 raporu birlestirir.
- **2 Aralik 22:00:** 10 kisilik ekip provasi (12 dk sunum + canli demo, 8 dk bireysel kod soru-cevap provasi).
- **3 Aralik:** Son hata kontrolleri, GitHub commit gecmisi kontrolu ve teslim.

## GitHub Commit Hatirlatmasi

Hoca GitHub `Commit History` ve `Contributor Insights` kismini kontrol edecegi icin her ekip uyesi:
1. Kendi bilgisayarindan, kendi GitHub hesabiyla commit atmalidir.
2. Tum kodu tek bir commit ile son gun atmak yerine en az 3-4 anlamli commit (ornek: taslak fonksiyonlar, algoritma implementasyonu, test/duzeltme) yapmalidir.
