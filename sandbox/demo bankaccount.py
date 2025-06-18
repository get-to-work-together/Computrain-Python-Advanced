class Bankaccount:

    def __init__(self, holder, iban, balance = 0.0):
        self.__holder = holder
        self.__iban = iban
        self.__balance = balance

    def __del__(self):
        print('Account closed')

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def info(self):
        print(f'Account IBAN: {self.__iban} belonging to {self.__holder} has a balance of {self.__balance}.')

# ------------------------------------------------------

acc1 = Bankaccount('Peter', 'NL99ABCD0123476543')


print(dir(acc1))

acc1.deposit(1000)
acc1.withdraw(230)
acc1.info()

del acc1