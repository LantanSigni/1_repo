text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
dict_counter = {}  # {'L':1, ...}
for char in text:
    #    try:
    #        count = dict_counter[char]  # getting value by key
    #    except KeyError:
    #        count = 0
    count = dict_counter.get(char, 0)
    count += 1
    dict_counter[char] = count  # writing value by key

print(dict_counter)
