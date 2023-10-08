password = input()
if 'qwerty' in password or '123' in password:
    print('This password is weak!')
if len(password) < 8:
    print('Pass is too short')
else:
    print('Your password is ok')
