def digit_count(number):
    sum = 0

    if (number == 0):

        return sum
    else:

        sum += number % 10
        return sum + digit_count(number // 10)


x = digit_count(789)

print(x)