def factorial(n):

    if n < 2:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):

    return int(factorial(n)/(factorial(n - k) * factorial(k)))


n = int(input())
k = int(input())
print(number_of_groups(n, k))
