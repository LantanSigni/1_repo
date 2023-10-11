while True:
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))

    gcd = min(first, second)

    while first >= 0 and second >= 0:
        if first % gcd == 0 and second % gcd == 0:
            print(gcd)
            break
        elif first % gcd > 0 or second % gcd > 0:
            gcd = gcd - 1
        else:
            print('Error')
            break
