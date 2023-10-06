x = input()


def func():
    x = 4
    print('Зміна локального x на', x)  # Зміна локального x на 2


func()
print('x як і раніше', x)   # x як і раніше 30
