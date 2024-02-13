def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
        return True


def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)