def invite_to_event(username):
    if username:
        print(f"Dear {username}, we have the honour to invite you to our event.")
    else:
        print("Username cannot be empty. Please try again.")


username = input("Введіть ім'я: ")
invite_to_event(username)
