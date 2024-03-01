t1 = [1, 1, 5, 10]
t2 = [10, 2]
t3 = [1, 1, 1]

terra = [t1, t2, t3]
power = 1


def game(terra, power):
    for sublist in terra:
        for item in sublist:
            if item <= power:
                power = power + item
            elif item > power:
                break
    return power


print(game(terra, power))
