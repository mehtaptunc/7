#Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if(a>=b and a>=c):
    print("En büyük sayı a dır")
elif(b>=a and b>=c):
    print("En büyük sayı b dir")
elif(c>=a and c>=b):
    print("En büyük sayı c dir")
