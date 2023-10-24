a = [1, 2]
b = [3, 4, a]

print(b)  # 3, 4, [1, 2]
print(b[2])  # [1, 2]

a[0] = 5  # [5, 2]

print(b)  # 3, 4, [5, 2]

b.append('hello')

print(b)
print(b[2])  # 0 = 3, 1 = 4, 2 = [1, 2] - indexes start from 0
