numbers = ['a', 'b']
numbers.append('v')
print(str(numbers) + ' *list a, b, v')

num = ['1', '2']
num.clear()
print(str(num) + ' *empty list')

num = ['1', '2', '3']

chars = ['a', 'b', 'c']

chars.remove('b')
print(str(chars) + ' *removed B')
last = chars.pop(1)
print(chars)
print(last)
chars.extend(num)
print(chars)

c_ind = chars.index('1')
print(c_ind)

chars.append('a')
print(chars)

a_count = chars.count('a')
print(a_count)

chars.append('g')
chars.append('6')
print(str(chars) + ' *added g and 6')

chars.sort()
print(str(chars) + ' *sorted!')
