saniye = int(input("Saniye: "))

gun = saniye // 86400
kalan_saniye1 = saniye % 86400

saat = kalan_saniye1 // 3600
kalan_saniye2 = saniye % 3600

dakika = kalan_saniye2 // 60
son_kalan_saniye = kalan_saniye2 % 60

print(saniye, "saniye =", gun, "gün", saat, "saat", dakika, "dakika", son_kalan_saniye, "saniye")