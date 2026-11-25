# Modul 2: Bilgili (Sezgisel) Arama Algoritmalari (Greedy Best-First, A*)
# Sorumlu: Rol 4 (Bilgili Arama Algoritmalari Sorumlusu)

from src.veri_yapilari import AramaSonucu


def sezgisel_hesapla(graf, dugum, hedef, yontem="manhattan"):
    # TODO (Rol 4): Manhattan veya Kus Ucusu (SLD / Oklid) mesafesini hesapla.
    return 0.0


def greedy_ara(graf, baslangic, hedef, yontem="manhattan"):
    # TODO (Rol 4): OPEN ve CLOSED listelerini tutarak Greedy Best-First Search yaz.
    return AramaSonucu(
        algoritma_adi="Greedy Best-First (Taslak)",
        yol=[baslangic, hedef],
        toplam_maliyet=0.0,
        genisletilen_dugum=0,
        sure_ms=0.0,
    )


def a_star_ara(graf, baslangic, hedef, yontem="manhattan"):
    # TODO (Rol 4): f(n) = g(n) + h(n) ile OPEN ve CLOSED listelerini tutarak A* yaz.
    return AramaSonucu(
        algoritma_adi="A* (Taslak)",
        yol=[baslangic, hedef],
        toplam_maliyet=0.0,
        genisletilen_dugum=0,
        sure_ms=0.0,
    )
