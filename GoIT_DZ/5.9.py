def formatted_numbers():
    result = []
    result.append(f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|")
    for i in range(16):
        hexd = hex(i)[2:]
        bind = bin(i)[2:]
        result.append(f"|{i:<10}|{hexd:^10}|{bind:>10}|")
        i += 1
    print(result)


for el in formatted_numbers():
    print(el)
