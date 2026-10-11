import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu
from uzay_oyunu.kayit import gorev_kaydi
from uzay_oyunu.oyun import galaksi_kur, harita_yukle

def test_envanter_metni() -> None:
    """envanter metninin dogru calıstıgını test eder""" 
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"
    assert envanter_metni(False, False, False) == ""
    assert envanter_metni(True, True, True) == "Sende: bol kredi, hiperdrive, yetenekli bir pilot"

def test_hedef_menusu() -> None:
    """hedef menüsünün numaralı bicimde çalıstigini test eder."""
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen

def test_gorev_kaydi() -> None:
    """gorev_kaydi fonksiyonunun doğrudan ve unpacking ile çalışmasını test eder."""
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"oncelik": "yüksek", "sorumlu": "Ayşe"}
    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        "1. Kredi kazan\n"
        "2. Pilot bul\n"
        "3. Hiperdrive al\n"
        "sorumlu: Ayşe"
    )
    assert gorev_kaydi("Kara deliğe atla", *adimlar, **ekler) == beklenen

def test_galaksi_kur() -> None:
    """galaksi_kur fonksiyonunun JSON verisi, varsayılan yakıt ve ValueError durumlarını test eder."""
    g = harita_yukle()
    assert (g["konum"], g["yakit"]) == ("dünya", 100)

    assert galaksi_kur(["mars"], {"mars": []}, "mars")["yakit"] == 50

    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "venüs")