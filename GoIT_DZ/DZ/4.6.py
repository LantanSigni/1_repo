def split_list(grade):
    high_list = []
    low_list = []
    if grade:
        list_middle = int(sum(grade) / len(grade))
    else:
        return ([], [])
    for i in grade:
        if i > list_middle:
            high_list.append(i)
        else:
            low_list.append(i)
    return (low_list, high_list)


grade = (12, 10, 8, 8, 6, 3, 7, 11, 7, 9)
print(split_list(grade))
