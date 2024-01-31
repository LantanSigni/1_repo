users = {
    "Alice": "C00peR",
    "Bob": "uNc1e",
    "Carl": "ClariNet"
}

input_password = input("Enter your password, please: ")

if input_password in users.values():
    user_login = next(key for key, value in users.items()
                      if value == input_password)
    print(f"Welcome, {user_login}! It's nice to see you again.")
else:
    print("Sorry, I don't know you.")
