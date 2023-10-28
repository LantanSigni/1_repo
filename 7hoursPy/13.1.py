def count_list(par, par2=False, count=0):  # parametr
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count


j = [9, 8, 7, 6]

h, p = count_list(j, 1)

print(count_list(j, count=-1))  # par2 does not change, prints 3
print(count_list(j, 1))  # par2 - True, prints 4 int

print(h, p)
