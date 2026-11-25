# Modul 2: Bilgisiz Arama Algoritmalari (BFS, DFS/IDS, UCS)
# Sorumlu: Rol 3 (Bilgisiz Arama Algoritmalari Sorumlusu)

from src.veri_yapilari import AramaSonucu


def bfs_ara(graf, baslangic, hedef):
    # TODO (Rol 3): OPEN ve CLOSED listelerini tutarak BFS algoritmasini sifirdan yaz.
    # Sureyi time.perf_counter() ile ms cinsinden olc ve AramaSonucu dondur.
    return AramaSonucu(
        algoritma_adi="BFS (Taslak)",
        yol=[baslangic, hedef],
        toplam_maliyet=0.0,
        genisletilen_dugum=0,
        sure_ms=0.0,
    )


def dfs_ara(graf, baslangic, hedef):
    # TODO (Rol 3): OPEN ve CLOSED listelerini tutarak DFS (veya IDS) algoritmasini sifirdan yaz.
    return AramaSonucu(
        algoritma_adi="DFS (Taslak)",
        yol=[baslangic, hedef],
        toplam_maliyet=0.0,
        genisletilen_dugum=0,
        sure_ms=0.0,
    )


def ucs_ara(graf, baslangic, hedef):
    # TODO (Rol 3): Oncelik kuyrugu (OPEN) ve CLOSED listesi ile UCS algoritmasini sifirdan yaz.
    return AramaSonucu(
        algoritma_adi="UCS (Taslak)",
        yol=[baslangic, hedef],
        toplam_maliyet=0.0,
        genisletilen_dugum=0,
        sure_ms=0.0,
    )
