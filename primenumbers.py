import math


def isPrime(number):

    if number % 2 == 0:
        return False

    if number == 2:
        return True

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True


