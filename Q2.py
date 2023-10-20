import time

x = time.time()

a = 1
b = 1

sum = 0

while(b < 4_000_000):


    c = a + b
    a = b
    b = c
    #a,b=b,a+b şeklinde de yazılabilir bu denklemler.


    print(b)

    if(b % 2 == 0):

        sum += b

print("sum:",sum)



y = time.time()

print(y-x)