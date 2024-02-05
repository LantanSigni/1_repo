import os

# set active directory as current location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


class RandomGenerator:
    def __init__(self, initial_state):
        if (initial_state < 0) or (initial_state > 255):
            raise Exception("Initial state must be integer in range [0; 255]")
        '''Як бачиш з коду ми будемо перезаписувати файл по байтах, тому якщо на вході
        буде некоректні дані, які не є цілим числом або більше за байт — ми будемо
        генерувати свою власну виключну ситуацію'''
        self.state = initial_state

    def get_rand(self):
        self.state = (self.state * 37 + 73) % 256
        return self.state


if __name__ == '__main__':
    try:
        generator = RandomGenerator(42)
    except Exception as e:
        print(f'Exception occured! {e.args[0]}')

    with open("secret.txt") as secret:
        file_content = secret.read()
        secret_length = len(file_content)

    with open("secret.txt", 'wb+') as secret:
        for i in range(10):
            mask = generator.get_rand().to_bytes(
                1, 'big', signed=False)  # переведення в байти
            secret.seek(0)
            for j in range(0, secret_length):
                secret.write(mask)
