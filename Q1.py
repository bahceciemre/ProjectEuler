def bolen(sayi):

    toplam = 0

    for i in range(1,sayi):

        if (i % 3 == 0 or i % 5 == 0):

            toplam += i

    return toplam

say = int(input("Lütfen sayı giriniz: "))

a = bolen(say)


print(a)