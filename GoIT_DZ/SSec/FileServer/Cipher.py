import os

# set active directory as current location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


class Cipher:
    def __init__(self, key):
        if (key < 0) or (key > 255):
            raise Exception("Key must be integer in range [0; 255]")
        self.key = key

    # Зашифровує 1 байт
    def encrypt_byte(self, data_byte):
        return data_byte ^ self.key

    # Розшифровує 1 байт
    def decrypt_byte(self, encrypted_data_byte):
        return encrypted_data_byte ^ self.key


if __name__ == '__main__':
    encrypted_content = bytearray(0)
    decrypted_content = bytearray(0)
    cipher = Cipher(42)

    with open("secret.txt", 'rb+') as secret:
        data_byte = secret.read(1)  # Читання по одному байту
        while data_byte:  # Читаємо увесь файл, доки не закінчаться символи
            encrypted_byte = cipher.encrypt_byte(data_byte[0])
            # Шифрування поточного байту
            encrypted_content.append(encrypted_byte)  # Накопичення результату
            data_byte = secret.read(1)  # Читання наступного байту

    with open("encryptedSecret.txt", 'wb+') as enc_secret:
        enc_secret.write(encrypted_content)

    with open("encryptedSecret.txt", 'rb') as enc_secret:
        encrypted_content = enc_secret.read()

    for encrypted_byte in encrypted_content:
        decrypted_byte = cipher.decrypt_byte(encrypted_byte)
        decrypted_content.append(decrypted_byte)

    with open("revealedSecret.txt", 'wb') as revealed_secret:
        revealed_secret.write(decrypted_content)
