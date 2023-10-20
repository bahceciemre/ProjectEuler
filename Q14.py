def Collatz(number):
    count = 1
    if (number % 2 == 0):
        count += 1
        return Collatz(number/2)
