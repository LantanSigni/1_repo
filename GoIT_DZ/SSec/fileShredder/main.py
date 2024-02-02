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
        generator = RandomGenerator(256)
    except Exception as e:
        print(f'Exception occured! {e.args[0]}')

    with open("secret.txt", 'w') as secret:
        file_content = secret.write(
            'The quick brown fox jumps over the lazy dog')

    with open("secret.txt", 'r') as secret:
        file_content = secret.read()
        print(file_content)
