class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello! I am {self.name}."


bill = Human('Bill')
print(bill.say_hello())  # Hello! I am Bill.
print(bill.age)         # 0

jill = Human('Jill', 20)
print(jill.say_hello())  # Hello! I am Jill.
print(jill.age)         # 20


class Secret:
    public_field = 'this is public'
    _private_field = 'avoid using this please'
    __real_secret = 'I am hidden'


s = Secret()
print(s.public_field)
print(s._private_field)
print(s._Secret__real_secret)


class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print("Only numbers greater than zero accepted.")


p = PositiveNumber()
p.value = 1
print(p.value)       # 1
p.value = -1         # Only...
p._PositiveNumber__value = -1
print(p.value)       # -1
