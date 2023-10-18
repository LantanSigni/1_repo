def calculate_sum(x):

    y = 3

    return x + y


result = calculate_sum(5)
print(result)  # 8
print('-------')

########################


def calculate_sum1(x, y):

    return x + y


result = calculate_sum1(10, 2)
print(result)  # 12
print('-------')

#########################


def calculate_diff(x, y):

    return x - y


result = calculate_diff(y=10, x=2)
print(result)  # -8
print('-------')

########################


def calculate_diff1(x, y=5):

    return x - y


result = calculate_diff1(2, 10)  # 10 has priority for y
print(result)  # -8
print('-------')

#######################


def calculate(*args):

    for arg in args:
        print(arg)

    return args


result = calculate(1, 2, 3, 4, 5, 6, 7)
print('-------')

#########################


def calculate1(**kwargs):

    return kwargs


result = calculate1(a=5, b=7, c=2)
print(result)
print('-------')

#########################
