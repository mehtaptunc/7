#Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
# Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
def mukemmel(sayi):
  
    toplam=0
    for i in range(1,sayi):
        if(sayi% i ==0):
            toplam +=i
    if toplam==sayi:
        print(f"{sayi} Mükemmel sayıdır")   
    else:
        print(f"{sayi} Mükemmel sayı değildir.") 
sayi=int(input("Sayı: "))  
mukemmel(sayi)       