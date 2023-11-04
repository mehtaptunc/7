#Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
#1-Kullanıcıdan bir sayı girmesini isteriz
#2-Girilen sayıyı bölecek olan sayıları tutacak bir değişken oluşturup(bölen) 2 sayısını ata.
#3-Girilen sayıya kadar döngü oluştur
#4-Eğer girdiğimiz sayı bölen değişkenine bölünüyorsa ekrana bölen değişkeninin değerini yazdırıyoruz ve girdiğimiz sayıyıda bölüyoruz 
#5-Eğer sayımız bölen değişkenine tam bölünmüyorsa bölen değişkenin değerini 1 artırıyoruz.
def asal_carpanlari_bul(sayi):   
    carpanlar = []
    bolen = 2
    
    while sayi > 1:
        while sayi % bolen == 0:      
            carpanlar.append(bolen)    
            sayi //= bolen    
        bolen += 1
    
    return carpanlar

sayi = int(input("Bir sayı giriniz: "))

if sayi < 2:
    print("2 veya daha büyük bir sayı giriniz.")
else:
    asal_carpanlar = asal_carpanlari_bul(sayi)
    print(f"{sayi}'nin asal çarpanları: {asal_carpanlar}")