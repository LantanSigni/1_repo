m = 'string text'
count = 0

for i in m:
    if i == 't':
        print('It has letter t')
        count += 1

    if i == 'i':
        break

else:
    print('Cycle is finished, there are', count, 't.')

print('It keeps working.')
