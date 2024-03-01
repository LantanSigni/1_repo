class User:
    '''Створення класу Юзер, гостя за замовчеванням, зі стандартним атрибутом логін.
    Також декларуємо метод привітання Юзера за його ім'ям'''
    login = 'Guest'

    def greet(self):
        print(f'Hi, my login is {self.login}.')


if __name__ == '__main__':  # перевірка класу User.
    alice = User()
    alice.greet()  # Hi, my login is Guest

    bob = User()
    bob.login = "Bob"
    bob.greet()  # Hi, my login is Bob


class AuthenticatedUser(User):
    '''Клас зареєстрованого користувача, який наслідує логін від Юзера та має свій атрибут пароля.
    Метод автентифікувати присвоює новий пароль зареєстрованому користувачу.'''
    password = 'password'

    def authenticate(self, user_password):
        if user_password == self.password:
            self.password = user_password
            return True
        else:
            return False


if __name__ == '__main__':  # перевірка класу AuthenticatedUser.

    alice = AuthenticatedUser()
    alice.greet()  # Hi, my login is Guest
    is_alice = alice.authenticate("password")
    # Is 'alice' a default AuthenticatedUser: True
    print(f"Is 'alice' a default AuthenticatedUser: {is_alice}")

    bob = AuthenticatedUser()
    bob.login = "Bob"
    bob.password = "uNc1e"
    bob.greet()  # Hi, my login is Bob
    is_bob = bob.authenticate("password")
    # Is 'bob' a default AuthenticatedUser: False
    print(f"Is 'bob' a default AuthenticatedUser: {is_bob}")


class AccessObject:
    '''Клас об'єкту, до якого надається доступ, зі своїм вмістом,
    назвою цього об'єкта та вказуванням поточного власника.'''
    content = ''
    name = ''
    owner = User()

    def change_owner(self, old_owner_password, new_owner):
        '''Метод передачі прав доступу від користувача до іншого користувача.
        Проводить перевірку належності обох користувачів до зареєстрованих користувачів та
        співпадіння вказаного паролю до паролю попереднього власника доступу.
        При проходженні всіх перевірок, назначається новий власник прав доступу'''
        if (isinstance(new_owner, AuthenticatedUser) and
            isinstance(self.owner, AuthenticatedUser) and
                old_owner_password == self.owner.password):
            self.owner = new_owner
            print(f'The ownership changing of {
                self.name} was successful! New owner is {self.owner.login}.')
        else:
            print(f'Unauthorised attempt of {
                  self.name} owner changing detected!.')


if __name__ == '__main__':  # Перевірка класу AccessObject.

    alice = AuthenticatedUser()
    alice.login = "Alice"
    bob = AuthenticatedUser()
    bob.login = "Bob"
    bob.password = "uNc1e"

    log = AccessObject()
    log.owner = alice
    log.name = "Computer logs"
    log.content = "There is no entries yet"

    security_policy = AccessObject()
    security_policy.owner = bob
    security_policy.name = "Enterprise security policy"
    security_policy.content = "Only authorized users may access objects"

    log.change_owner(bob.password, bob)
    security_policy.change_owner(bob.password, alice)
