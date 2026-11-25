# ISE 315 - Akilli Hastane ve Otonom Acil Mudahale Sistemi

Bu repo, ISE 315 Yapay Zekaya Giris dersi donem projesi icin hazirlanmistir. Projede bir hastane yerleskesinde acil vakalarin degerlendirilmesi, on tani cikarimi, kritik kaynak dagitimi ve en uygun rota hesaplamasi ders kapsamindaki temel yapay zeka yontemleriyle sifirdan kodlanmaktadir.

## Proje Klasor Yapisi

```text
Yz-giris-projesi/
|-- main.py                          # Programin baslangic dosyasi
|-- README.md                        # Proje ozeti ve calistirma bilgileri
|-- docs/
|   |-- mimari_ve_veri_akisi.md      # Moduller arasi veri akisi ve fonksiyon sozlesmeleri
|   |-- takvim_ve_gorev_dagilimi.md  # Ekip ici teslim tarihleri ve bagimliliklar
|-- src/
|   |-- veri_yapilari.py             # Tum modullerin kullandigi ortak siniflar
|   |-- sistem_koordinatoru.py       # Modulleri sirayla calistiran ana akis (Rol 1)
|   |-- modul1_ajan_peas/
|   |   |-- peas_analizi.py          # PEAS tablosu ve ortam ozellikleri (Rol 2)
|   |-- modul2_arama/
|   |   |-- graf.py                  # Hastane yerleske grafi (Rol 2)
|   |   |-- bilgisiz_arama.py        # BFS, DFS/IDS, UCS (Rol 3)
|   |   |-- bilgili_arama.py         # Greedy Best-First, A* ve sezgisel fonksiyonlar (Rol 4)
|   |-- modul3_minimax/
|   |   |-- oyun_agaci.py            # Kaynak paylasim agaci ve Minimax (Rol 5)
|   |   |-- alfa_beta.py             # Alfa-Beta budama ve analiz (Rol 6)
|   |-- modul4_kural_tabanli/
|   |   |-- bilgi_tabani.py          # Tibbi olgular, kurallar ve cakisma cozumu (Rol 7)
|   |   |-- cikarim_motoru.py        # Ileri/Geri zincirleme ve aciklama mekanizmasi (Rol 8)
|   |-- modul5_bulanik/
|   |   |-- bulanik_triyaj.py        # Uyelik fonksiyonlari, Mamdani, Centroid (Rol 9)
|   |-- arayuz/
|       |-- gui.py                   # Canli demo arayuzu (Rol 10)
|-- tests/
    |-- test_akis.py                 # Moduller arasi temel veri akisi testi
```

## Grup Rol Dagilimi

| No | Rol | Sorumlu Ogrenci | Ogrenci No | Sorumlu Oldugu Dosyalar |
|---|---|---|---|---|
| 1 | Proje Koordinatoru & Sistem Mimari | [Abdulsamet Özkan] | [B231200023] | `src/veri_yapilari.py`, `src/sistem_koordinatoru.py`, `main.py`, `docs/` |
| 2 | Ajan & Durum Uzayi Modelleme Uzmani | [Mesut Taha Güven] | [B231200039] | `src/modul1_ajan_peas/peas_analizi.py`, `src/modul2_arama/graf.py` |
| 3 | Bilgisiz Arama Algoritmalari Sorumlusu | [Burak Eren Karip] | [B241200019] | `src/modul2_arama/bilgisiz_arama.py` |
| 4 | Bilgili Arama Algoritmalari Sorumlusu | [Hidayet Opuz] | [B231200015] | `src/modul2_arama/bilgili_arama.py` |
| 5 | Rekabetci Arama & Minimax Sorumlusu | [Efekan Ocak] | [B241200035] | `src/modul3_minimax/oyun_agaci.py` |
| 6 | Alfa-Beta Budama & Analiz Sorumlusu | [Vahap Polat] | [B231200009] | `src/modul3_minimax/alfa_beta.py` |
| 7 | Mantiksal Bilgi Tabani Muhendisi | [Yaman Ustaoğlu] | [B241200555] | `src/modul4_kural_tabanli/bilgi_tabani.py` |
| 8 | Cikarim Motoru & Aciklama Modulu Sorumlusu | [Ahmet Can Alpay] | [B251210350] | `src/modul4_kural_tabanli/cikarim_motoru.py` |
| 9 | Bulanik Denetim & Matematiksel Modelleme | [Sonay Sude Savcı, Yıldıray Ali Kara] | [B241200069,B231210048] | `src/modul5_bulanik/bulanik_triyaj.py` |
| 10 | Arayuz (GUI) & Entegrasyon / Test Sorumlusu | [Oasid Mohammad] | [B241200554] | `src/arayuz/gui.py`, `tests/test_akis.py` |

## Calistirma

Projede harici kutuphane zorunlulugu yoktur, Python 3 standart kutuphaneleri ile calisir.

```bash
python main.py
```

Temel akis testini calistirmak icin:

```bash
python tests/test_akis.py
```

## GitHub Calisma Kurallari

- Kimse dogrudan `main` dalina (branch) push atmamalidir.
- Her uye kendi gorevi icin ayri bir branch acmalidir. Ornek: `rol3-bilgisiz-arama`, `rol9-bulanik-triyaj`.
- Kodlar son gun toplu atilmamali, yapilan her parca duzenli olarak commit edilmelidir.
- Gorev tamamlandiginda `main` dalina Pull Request (PR) acilir, Rol 1 kontrol edip birlestirir.
- `src/veri_yapilari.py` dosyasinda degisiklik gerekiyorsa once grupta konusularak karar verilir.
