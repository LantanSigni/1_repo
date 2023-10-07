chars = {'a': 1, 'b': 2}
b_num = chars.pop('b')
print(chars)  # Only 'a' is left
print(b_num)  # Prints "b"
chars.update({'b': 2, 'c': 3})
print(chars)    # Adds b and c
