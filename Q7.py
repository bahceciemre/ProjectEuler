def asal(sayi):

    flag = True

    i = 2

    while (i < sayi):

       if(sayi % i == 0):

           flag = False

       i += 1

    return flag

i = 0
a = 1
while (i != 10001):

    a +=1

    if (asal(a)):

        i+=1

        #print(a)
print("i:",i)

print("a:",a)

# Bu kod yaklaşık 5-10 dk çalıştı. İnternette bu kadar uzun mu kontrol et.



