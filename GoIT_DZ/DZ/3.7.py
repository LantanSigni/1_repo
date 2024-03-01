def first(size, *items):
    return size + len(items)


def second(size, **items):
    return size + len(items)


print(first(4, 1, 1, 1))
print(second(4, one='1', two='2'))
