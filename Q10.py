import time
import math
ini = time.time()

def asal(sayi):

    for i in range(2,int(math.sqrt(sayi)+1)):

        if(sayi % i == 0):

            return False


    else:

        return True

sum = 0

for i in range(2,2000000):

    if(asal(i)):

        sum += i

print(sum)

fin = time.time()

print(fin-ini)
