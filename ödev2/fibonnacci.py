"""
İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
"""
a = 1
b = 1

fibonacci = [a,b]
for i in range(18):


    a,b = b,a + b

    fibonacci.append(b)

print(fibonacci)

  

