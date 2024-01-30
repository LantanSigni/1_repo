class Acc:
    owner = ''
    balance = 0

    def init(self, _owner, _balance):
        self.owner = _owner
        self.balance = _balance

    def deposit(self, _sum):
        self.balance += _sum
        print(f'{self.owner} deposit {_sum}, your balance - {self.balance}')

    def withdraw(self, _sum):
        self.balance -= _sum
        print(f'{self.owner} withdraw {_sum}, your balance - {self.balance}')

    def say_balance(self):
        print(f'{self.owner}, your balance - {self.balance}')


tom = Acc()
sam = Acc()


tom.init('Tom', 500)
tom.say_balance()
sam.init('Sam', 1000)
sam.say_balance()

tom.withdraw(300)
tom.say_balance()
