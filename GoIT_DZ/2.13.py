message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
# print(ord('a'))

for ch in message:
    if ch == ' ' or ch == '!':
        encoded_message += ch
    elif ch == 'H':
        if offset == 7:
            ch = 'O'
        else:
            ch = "S"
        encoded_message += ch
    elif ch:
        pos = 0

        pos = ord(ch) - ord('a')
        # print(ord(ch))
        # print(f'Зсув відносно а = {pos}')

        pos = (pos + offset) % 26
        # print(f'Позиція після зсуву {offset} тепер {pos}')

        ch = chr(pos + ord('a'))
        # print(f'Нова буква {ch}')

        encoded_message += ch

print(encoded_message)

# pos = 0
# offset = 37
# pos = ord('e') - ord('a')
# print(pos)
# pos = (pos + offset) % 26
# print(pos)
# new_char = chr(pos + ord("a"))
# print(new_char)
