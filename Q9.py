#Pisagor Teoremi
import time

bas = time.time()
for c in range(1,1001):

    for b in range(1,c+1):

        for a in range(1,b+1):

            if (a + b + c == 1000 and a**2 + b**2 == c**2):

                print("***********")
                print("a:{}\nb:{}\nc:{}".format(a,b,c))
                print("***********")
                print("axbxc= ",a*b*c)


bit = time.time()


print(bit-bas)