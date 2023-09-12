from random import randint


def generate_random_numbers(n: int = 5) -> str:
    min = pow(10, n - 1)
    max = pow(10, n) - 1
    code = randint(min, max)
    return str(code)