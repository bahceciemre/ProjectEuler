"""""Recursive (Yineleme) Yöntemine Göre Yazılan Algoritma"""

def factorial(sayi):
    if (sayi == 0):
        return 1

    elif(sayi == 1):

        return 1
    else:
        return sayi*factorial(sayi-1)

def digit_count(sayi):
    sum = 0

    if(sayi == 0):

        return sum
    else:

        sum = sum + sayi % 10 + digit_count(sayi // 10)

    return sum

x = digit_count(factorial(100))

print(x)