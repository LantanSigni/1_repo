import config_protector
import json
import os

# set active directory as current location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def check_password(input_password):
    with open("config.json", "r") as config_json:
        config = json.load(config_json)

    password_tries = config["attemts"]
    while password_tries > 0:
        for user in config["users"]:
            if input_password == user["password"]:
                username = user["login"]
                print(f"Hello, {username}!")
                return True, username
        password_tries -= 1
        if password_tries > 0:
            print("Sorry, password is invalid. Try again!")
            print(f"{password_tries} attempt(s) left.")
            input_password = input("Enter your password, please: ")
        else:
            print('Sorry, I dont know you.')
            break
    return False


def main():
    input_password = input("Enter your password, please: ")
    input_password = check_password(input_password)
    hide_config = input("Create encrypted config? Y/N ")
    if hide_config == "Y":
        config_protector.hide_config_data(
            b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y=')
    show_config = input("Show encryted config? Y/N ")
    if show_config == "Y":
        config_protector.show_config_data(
            b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y=')


if __name__ == "__main__":
    main()
