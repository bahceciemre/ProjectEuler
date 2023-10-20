import time

ini = time.time()

def ters_cevir(sayi):

    sayi = str(sayi)

    if (sayi == sayi[::-1]):

        return True

    else:

        return False


max = 0

for i in range(100, 1001):

    for j in range(100, 1001):

        if (ters_cevir(i*j) and max < i*j):

            max = i*j

print(max)

fin = time.time()

print("Time for 4.1:",fin-ini)
