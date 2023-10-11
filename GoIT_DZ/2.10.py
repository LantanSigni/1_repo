num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    for i in range(num):
        sum = sum + num
        num = num - 1

    print(sum)
    num = int(input("Enter integer (0 for output): "))
