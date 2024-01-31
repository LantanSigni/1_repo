# Словник користувачів та їх паролів в не зашифрованому вигляді.
users = {
    "Alice": "C00peR",
    "Bob": "uNc1e",
    "Carl": "ClariNet"
}

# Функція перевірки пароля.


def check_password(input_password):
    password_tries = 3
# Цикл рахування використаних спроб.
    while password_tries > 0:
        # Якщо введений пароль = значенню зі словника - ф-я повертає значення Тру та останній введений пароль як кортеж.
        if input_password in users.values():
            return True, input_password
        # Якщо пароль не вірний - к-сть спроб зменьшується на одну.
        elif password_tries > 1:
            password_tries -= 1
            print("Sorry, password is invalid. Try again!")
            print(f"{password_tries} attempt(s) left.")
            input_password = input("Enter your password, please: ")
        # По закінченню спроб 3-х, коли рахівник = 1, цикл переривається.
        else:
            print('Sorry, I dont know you.')
            break
# Ф-я повертає значення кортежу, які нам ще знадобляться.
    return False, input_password

# Ф-я перевірки коду автентифікації. Як аргументи, приймає введений код автентифікації та останній введений пароль..


def check_auth_code(auth_code, input_password):
    # Для простоти код авт-ї = '1111' як рядок. Просто 1111 не приймався і я пів години бився, щоб це зрозуміти.
    # Тому що не можливо порівнювати '1111' з 1111 - рядок та цифри. Капець!
    # Потім буде перевірка типу даних, як додатковий захист.
    expected_auth_code = '1111'
    if auth_code == expected_auth_code:
        # Отримавши вірний код авт-ї, починаємо перебір значень і ключів, щоб знайти співпадіння і вивести потрібний ключ.
        user_login = next(key for key, value in users.items()
                          if value == input_password)
        print(f"Welcome, {user_login}! It's nice to see you again.")
    else:
        print("Intruder!")

# Головна ф-я.


def main():

    input_password = input("Enter your password, please: ")
    # Якщо не робити вивід ф-ї check_password у вигляді кортежа, то без перевірки нижче нічого не працює, якщо перша спроба провальна!
    # Адже перший введений пароль (не вірний, наприклад Cooper) залишається в пям'яті як глобальна змінна.
    # І вже повторний ввод пароль просто так його не оновлює, так як там вже використовується локальна змінна.
    # Це жесть, адже ще додатково 40+ хвилин битви, але дуже цікавої та повчальної!
    is_valid_password, input_password = check_password(input_password)
    # True, C00peR - правильні значення для першого користувача Alice, які повертає ф-я
    if is_valid_password:
        auth_code = input("Enter authentication code, please: ")
        check_auth_code(auth_code, input_password)


if __name__ == "__main__":
    main()
# Це було реально круто і цікаво!
