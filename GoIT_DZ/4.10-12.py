from random import randint


def get_random_password():
    password_length = 8
    password_characters = [chr(randint(40, 126))
                           for _ in range(password_length)]
    return ''.join(password_characters)


def is_valid_password(password):
    if len(password) != 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


def get_password():
    max_attempts = 100
    current_attempt = 0

    while current_attempt < max_attempts:
        current_attempt += 1
        random_password = get_random_password()

        if is_valid_password(random_password):
            return random_password

    raise ValueError(
        "Не вдалося згенерувати надійний пароль за вказану кількість спроб")


# Приклад використання:
secure_password = get_password()
print(secure_password)
