def counter(number):

    count = 0

    for i in range(1,number+1):

        if (number % i == 0):

            count += 1

    return count



i = 1

while True:

    triangle_number = i * (i + 1) * (0.5)
    triangle_number = int(triangle_number)

    if(counter(triangle_number) > 500):

        print(triangle_number)

        break
    i+=1
