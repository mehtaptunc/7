#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
## Palindromik sayı, iki taraftan okunduğu zaman okunuş yönüyle aynı olan sayılardır.

sayı = input("Bir Sayı Giriniz: ")
terssayı=sayı[::-1]

print("Girilen sayının tersi = %s" % (terssayı))
if terssayı == sayı:
    print("Girilen sayi palindromdur..")
else:
    print("Girilen sayi palindrom değildir.")