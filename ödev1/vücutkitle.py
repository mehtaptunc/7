#-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

isim = input("Lütfen isminizi giriniz:")
boy = float(input("Lütfen boyunuzu giriniz : "))
kilo = float(input("Lütfen kilonuzu  giriniz : "))
index = (kilo / boy ** 2)
print("Sayın {} beden kitle indeksiniz: {}".format(isim, index))


