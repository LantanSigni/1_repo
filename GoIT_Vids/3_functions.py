def calculate_sum():

    x = 3

    def inner_func():

        y = 5
        print(x)
        print(y)

    inner_func()


calculate_sum()


def outer_function():

    x = "outer"

    def inner_function():

        nonlocal x

        x = "inner"

    inner_function()

    print(x)  # Output: inner


outer_function()
