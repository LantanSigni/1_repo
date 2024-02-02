class AccessLevel:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

    def __gt__(self, other):
        return self.level > other.level


# if __name__ == '__main__':
#     unclassified = AccessLevel("Unclassified", 1)
#     secret = AccessLevel("Secret", 2)
#     top_secret = AccessLevel("Top Secret", 3)
#     print(unclassified < secret)  # True
#     print(secret == secret)  # True
#     print(unclassified > top_secret)  # False


class AccessObject:

    def __init__(self, name, content, access_level):
        self.name = name
        self.content = content
        self.access_level = access_level


class User:

    def __init__(self, login, mandatum):
        self.login = login
        self.__mandatum = mandatum

    def greet(self):
        print(f'Hi, my login is {self.login}.')

    @property
    def mandatum(self):
        return self.__mandatum.name

    @mandatum.setter
    def mandatum(self, new_mandatum):
        self.__mandatum = new_mandatum

    def get_access(self, access_object):
        if not access_object.access_level > self.__mandatum:
            print(f"Access granted. Content of the resource: {
                  access_object.content}")
        else:
            print("Access to Password Database denied!")


if __name__ == '__main__':
    unclassified = AccessLevel("Unclassified", 1)
    secret = AccessLevel("Secret", 2)
    top_secret = AccessLevel("Top Secret", 3)

    alice = User("Alice", top_secret)
    bob = User("Bob", unclassified)

    password_database = AccessObject(
        "Password Database",
        "Alice - C00peR, Bob - uNc1e",
        secret
    )

    alice.greet()
    alice.get_access(password_database)

    bob.greet()
    bob.get_access(password_database)
