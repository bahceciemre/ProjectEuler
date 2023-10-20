#Asal Çarpan Bulan Program

def asal(sayi):

    i = 2

    while True:

        if (sayi % i == 0):

            sayi = sayi/i


        elif (sayi % i != 0):

            i+=1

        if (sayi == 1):

            return i

            break


sayi = int(input("Lütfen bir sayı giriniz: "))

a = asal(sayi)

print(a)