result = None
operand = None
operator = None
wait_for_number = True

while True:

    if wait_for_number == True:
        operand = input('Input number: ')

        try:
            operand = int(operand)
            if operator == None:
                result = operand
                wait_for_number = False
                continue
            elif operator == '+':
                result = result + operand
                wait_for_number = False
                print(result)
                continue
            elif operator == '-':
                result = result - operand
                wait_for_number = False
                print(result)
                continue
            elif operator == '*':
                result = result * operand
                wait_for_number = False
                print(result)
                continue
            elif operator == '/':
                result = result / operand
                wait_for_number = False
                print(result)
                continue
        except ValueError:
            print('Expecting number.')

    elif wait_for_number == False:
        operator = input("Input + or - or * or /: ")

        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            wait_for_number = True
            continue
        elif operator == '=':
            print(result)
            break
        else:
            print('Wrong operator.')
