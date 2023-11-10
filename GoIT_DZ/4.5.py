def lookup_key(dictionary, value):
    keys_list = []
    for key, val in dictionary.items():
        if val == value:
            keys_list.append(key)
    return keys_list


# Приклад використання:
my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
search_value = 1
result = lookup_key(my_dict, search_value)

print(f"Значення {search_value} знаходиться за ключами: {result}")
