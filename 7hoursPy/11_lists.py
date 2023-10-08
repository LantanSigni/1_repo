# m = [1, 2, 1, 3, 5, 'a', [3, 3, 4], ['s', 'r']]

# m[6] = 9

# print(m)

# m[0] += 2

# # print(len(m[6]))
# # print(m[-1][0])
# print(m)

# m[1], m[2] = m[2], m[1]
# print(m)

# m = m + [7]

# print(m)

# n = list('line')
# print(n)

# m += n
# print(m)

# r = list(range(10))

# print(r)

# s = []

# for i in r:
#     if i == 8:
#         continue
#     s += [i]
# else:
#     print(s)

x = [9, 8, 7, 6, 5]
x.append(4)
x.insert(1, 7)
print(x.count(7))
x.sort()
x.reverse()
y = x.pop(0)
print(y)
x.remove(7)
x.clear()
x.extend(['a', 's'])
h = x.copy()
print(h)
print(x)
