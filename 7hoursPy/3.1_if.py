x = 5

if x == 0:
    x = 1
    print('x is zero')

elif type(x) == type(5) or type(x) == type(5.5):
    print('x is ok')

else:
    print('this x is invalid')
    x = 1

print(100/x)
