


#Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

#Kullanıcıdan sayıları alalım:
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

#EBOB ve EKOK'u hesaplayalım:
a = sayi1
b = sayi2

while b:
    a, b = b, a % b

ebob_sonuc = a
ekok_sonuc = (sayi1 * sayi2) // ebob_sonuc
print(f"{sayi1} ve {sayi2} için EBOB: {ebob_sonuc}")
print(f"{sayi1} ve {sayi2} için EKOK: {ekok_sonuc}")
