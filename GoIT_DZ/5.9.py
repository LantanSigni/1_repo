def formatted_numbers():
    result = []
    result.append(f"|{'decimal':^10}|{'hex':^10}|{'binary':^10}|")
    for i in range(16):
        hexd = format(i, 'x')
        bind = format(i, 'b')
        result.append(f"|{i:<10}|{hexd:^10}|{bind:>10}|")
        # result += [f"|{i:<10}|{hex(i)[2:]:^10}|{bin(i)[2:]:>10}|" for i in range(16)]
    return result


for el in formatted_numbers():
    print(el)
