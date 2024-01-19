import hashlib
import getpass

users = {
    "Alice": hashlib.sha256("C00peR".encode()).hexdigest(),
    "Bob": hashlib.sha256("uNc1e".encode()).hexdigest(),
    "Carl": hashlib.sha256("ClariNet".encode()).hexdigest()
}

input_password = getpass.getpass("Enter your password, please: ")

hashed_password = hashlib.sha256(input_password.encode()).hexdigest()
print(hashed_password)

if hashed_password in users.values():
    user_login = next(key for key, value in users.items()
                      if value == hashed_password)
    print(f"Welcome, {user_login}! It`s nice to see you again.")
else:
    print("Sorry, I don`t know you.")
