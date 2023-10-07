some_iterable = ['a', 'b', 'c']
first_letter = some_iterable[0]
middle_letter = some_iterable[1]
last_letter = some_iterable[2]
print(first_letter, middle_letter, last_letter)

some_iterable[1] = 'Z'
print(some_iterable)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[0:9:2]
print(odd_numbers)
even_numbers = numbers[1:9:2]
print(even_numbers)
three_numbers = numbers[2:9:3]
print(three_numbers)

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:9:3]

numbers_copy = numbers[:]

print(numbers_copy)
