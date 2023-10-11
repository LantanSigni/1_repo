from random import randint

SIZE_X = 5
SIZE_Y = 5

char_x = randint(0, SIZE_X - 1)
char_y = randint(0, SIZE_Y - 1)
char_sign = 'X'

exit_x = randint(0, SIZE_X - 1)
exit_y = randint(0, SIZE_Y - 1)

turns = 0

while True:

    w_map = ''
    win_condition = char_x == exit_x and char_y == exit_y

    if win_condition:
        char_sign = 'W'

    for j in range(SIZE_Y):
        row = '|'

        for i in range(SIZE_X):

            if char_x == i and char_y == j:
                row += f'{char_sign}|'

            elif exit_x == i and exit_y == j:
                row += 'O|'
            else:
                row += ' |'

        w_map += f'{row}\n'

    print(w_map)

    if win_condition:
        print(f'You WON in {turns} turns!')
        break

    move = input('Enter direction (u | d | l | r): ')
    if move == 'u' and char_y > 0:
        char_y -= 1
    elif move == 'd' and char_y < SIZE_Y - 1:
        char_y += 1
    elif move == 'l' and char_x > 0:
        char_x -= 1
    elif move == 'r' and char_x < SIZE_X - 1:
        char_x += 1

    turns += 1
