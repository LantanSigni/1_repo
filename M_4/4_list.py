a = set('hello')
print(a)

b = {1, 2, 4, 5, 2, 4}
print(b)
b.add(3)
print(b)
b.remove(5)
print(b)

a = set('hello')
print(a)
b = set('Hi there!')
print(b)

AND = a & b
print(AND)
XOR = a ^ b
print(XOR)
OR = a | b
print(OR)
