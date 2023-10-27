#Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi= int(input("Lütfen bir sayi giriniz: "))
def asalSayiBul(sayi):
    
    isPrime = True
    if sayi <= 1 :
        isPrime = False
    for i in range (2, sayi):
        if sayi % i ==0:
            isPrime = False

    if isPrime == True: 
        print(sayi, "Asal Sayidir.")
    else:
        print(sayi, "Asal Sayi Değildir.")

print(asalSayiBul(sayi))

    
    
    

    

   
   
  
   
   
   
   
   
   
   
  