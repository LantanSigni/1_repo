def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) + 1


n = int(input("Choose your number: "))
print(fibonacci(n))
