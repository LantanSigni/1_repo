def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')


print_max(4, 16)  # пряма передача значень

# x = 5
# y = 7

x = input()
y = input()
print_max(x, y)  # передача змінних у якості аргументів
