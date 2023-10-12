result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        operand = int(operand)
        result += operand
    except ValueError:
        print(f"{operand} is not a number. Try again.")

    operator = input('Введіть дію: ')
    if operator != '+' or operator != '-' or operator != '*' or operator != '/':
        print(f'{operator} is not '+' or '-' or '/' or '*'. Try again')
