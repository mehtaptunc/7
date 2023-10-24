#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas=float(input("Maaş:"))
zamoranı=float(input("Zam oranı:"))

zamlımaas=maas+maas*(zamoranı/100)
print("Zamlı yeni maaş:",zamlımaas)