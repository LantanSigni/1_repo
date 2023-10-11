in_pin = '1234'
try_number = 0

while try_number < 3:

    user_pin = input('Enter your PIN: ')

    if len(user_pin) == 4 or len(user_pin) == 6:

        if in_pin == user_pin:

            amount = input('How much?: ')

            if amount > 0:
                print(f'Take your {amount}')
                break

        else:

            print('Sorry, wrong pin, try again, please.')
            print(f'You have {2 - try_number} tries.')
            try_number += 1

    else:
        print('4 or 6 digits for PIN.')

print('Good bye!')

# in_pin = '1234'

# for i in range(3):

#     user_pin = input('Enter your PIN: ')

#     if len(user_pin) == 4 or len(user_pin) == 6:

#         if in_pin == user_pin:
#             print('Here is your money.')
#             break
#         else:
#             print('Sorry, wrong pin, try again, please.')

#     else:
#         print('4 or 6 digits for PIN.')

# print('Good bye!')
