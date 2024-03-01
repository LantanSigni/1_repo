num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num > 0 and num <= 100:
    sum = sum + num
    # print(sum)
    num = num - 1
else:
    print(sum)
