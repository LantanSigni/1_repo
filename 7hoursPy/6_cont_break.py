x = ''

while len(x) < 5:
    y = input('Input data: ')
    if y == 'o':
        continue
    if y == 'l':
        break

    x += y

else:
    print(x)

print('Program works.')
