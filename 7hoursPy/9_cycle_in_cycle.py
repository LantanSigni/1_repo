x = 'abcdefghijklmnopqrstuvwxyz'
y = input('Inpur text:\n')

for i in x:
    count = 0
    for r in y:
        if i == r:
            count += 1
    if count > 0:
        print('There are', count, 'letter', i, '.')
