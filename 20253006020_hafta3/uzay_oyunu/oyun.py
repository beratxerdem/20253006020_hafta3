def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """esya varsa sende ... metnini, yoksa boş metin döndürür"""
    esyalar: list[str] = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("hiperdrive")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""

    return "Sende: " + ", ".join(esyalar)

def hedef_menusu(hedefler: list[str]) -> str:
    """gezegenleri numarali menü olarak döndürür."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)


def travel() -> None:
    """oyunun seyahat fonksiyonu"""
    planet = "dünya"
    credits = False
    engines = False
    copilot = False

    while True:
        print(f"\nŞuan ki gezegen: {planet}")
        metin = envanter_metni(credits, engines, copilot)
        if metin:
            print(metin)

        if planet == "dünya":
            destinations = ["centauri", "sirius"]
        elif planet == "centauri":
            credits = True
            destinations = ["dünya", "sirius", "orion"]
        elif planet == "sirius":
            engines = True
            destinations = ["dünya", "centauri", "orion", "kara_delik"]
        elif planet == "orion":
            copilot = True
            destinations = ["centauri", "sirius"]
        elif planet == "kara_delik":
            if credits and engines and copilot:
                print("Tebrikler!!! Oyunu Kazandin!!!")
            else:
                print("Donanımın eksik, kara delikte kayboldun!")
            break
        else:
            break
        print(hedef_menusu(destinations))
        secim = input("Seçiminiz (çikmak için 'q'): ")
        if secim == "q":
            break
        if secim.isdigit() and 1 <= int(secim) <= len(destinations):
            planet = destinations[int(secim) - 1]
        