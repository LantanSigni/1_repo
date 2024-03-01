from cryptography.fernet import Fernet
import json
import os

# set active directory as current location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


def hide_config_data(key):

    key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
    cipher = Fernet(key)

    with open("config.json", "r") as config_json:
        config_string = config_json.read()

    parsed_config = json.loads(config_string)

    for i in range(len(parsed_config["users"])):
        encrypted_users_login = cipher.encrypt(
            parsed_config["users"][i]["login"].encode())
        parsed_config["users"][i]["login"] = encrypted_users_login.decode()

        encrypted_users_password = cipher.encrypt(
            parsed_config["users"][i]["password"].encode())
        parsed_config["users"][i]["password"] = encrypted_users_password.decode()

    protected_config = json.dumps(parsed_config, indent=2)

    with open("protected_config.json", "w") as protected_config_json:
        protected_config_json.write(protected_config)


def show_config_data(key):

    key = b'5tlOpu2Bvib0m_yllgmzfhYVmonJNUR7bKCcdNh827Y='
    cipher = Fernet(key)

    with open("protected_config.json", "r") as protected_config_json:
        protected_config = protected_config_json.read()

    parsed_protected_config = json.loads(protected_config)

    for i in range(len(parsed_protected_config["users"])):
        encrypted_users_login = cipher.decrypt(
            parsed_protected_config["users"][i]["login"].encode())
        parsed_protected_config["users"][i]["login"] = encrypted_users_login.decode(
        )

        encrypted_users_password = cipher.decrypt(
            parsed_protected_config["users"][i]["password"].encode())
        parsed_protected_config["users"][i]["password"] = encrypted_users_password.decode(
        )

    decrypted_config = json.dumps(parsed_protected_config, indent=2)

    with open("decrypted_config.json", "w") as protected_config_json:
        protected_config_json.write(decrypted_config)
