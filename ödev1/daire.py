#Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

yarıçap=int(input("Lütfen yarıçap giriniz:"))
pi=3.14
alan=pi*(yarıçap**2)
çevre=2*pi*yarıçap
print("Dairenin alanı: {}" " Dairenin Çevresi:{}".format(alan,çevre))