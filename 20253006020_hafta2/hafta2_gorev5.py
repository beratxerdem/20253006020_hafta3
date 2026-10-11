anapara = float(input("Lütfen anaparayı girin: "))
yillik_faiz = float(input("Lütfen yıllık faizi (%) girin: "))
sure = int(input("Lütfen kaç yıl tutacagınızı girin: "))

son_deger = anapara*(1+(yillik_faiz/(12 * 100)))**(12 * sure)

son_deger = round(son_deger, 2)

print("Anapara (TL): ",anapara)
print("Yıllık faiz (%): ", yillik_faiz)
print("Süre (yıl): ", sure)
print("Gelecekteki Değer: ", son_deger)
