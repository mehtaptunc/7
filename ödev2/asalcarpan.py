#Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
#1-Kullanıcıdan bir sayı girmesini isteriz
#2-Girilen sayıyı bölecek olan sayıları tutacak bir değişken oluşturup(bölen) 2 sayısını ata.
#3-Girilen sayıya kadar döngü oluştur
#4-Eğer girdiğimiz sayı bölen değişkenine bölünüyorsa ekrana bölen değişkeninin değerini yazdırıyoruz ve girdiğimiz sayıyıda bölüyoruz 
#5-Eğer sayımız bölen değişkenine tam bölünmüyorsa bölen değişkenin değerini 1 artırıyoruz.
sayi=int(input("Bir sayı Giriniz."))
bölen=2
for i in range(1,sayi):
    if(sayi% bölen==0):
      print(bölen)
      sayi/=bölen
    else:
     bölen+=1     
          