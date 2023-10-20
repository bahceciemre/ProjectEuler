"""""Recursive (Yineleme) Yöntemine Göre Yazılan Daha Gelişmiş Bir Algoritma [Githubden alındı]"""

def digit_sum(number,sum):

  if (number == 0):

    return sum

  else:

    return digit_sum(number//10,number % 10 + sum)



def factorial(number,product):

  if (number == 0):

    return product

  elif(number == 1):

    return product

  else:

    return factorial(number-1,number*product)

print(digit_sum(factorial(100,1),0))
