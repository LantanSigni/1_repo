my_list = ['a', 'b', 'c', 'd', 'e', 'f']

for i in my_list:  # just elements
    print(i)

for i in range(len(my_list)):  # elements by index
    print(my_list[i])

for index, element in enumerate(my_list):  # print index + element
    print(index, element)

for i in reversed(my_list):  # reverse, same for sorted
    print(i)
