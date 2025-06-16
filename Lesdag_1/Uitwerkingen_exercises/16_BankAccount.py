class BankAccount:

    def __init__(self, balance, holder):
        self.__balance = balance
        self.__holder = holder

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        self.__balance = self.__balance - amount

    def info(self):
        return "Balance: {} \tHolder: {}".format(self.__balance, self.__holder)


ba1 = BankAccount(500.00, "Martijn Jansen")
print(ba1.info())

ba2 = BankAccount(100.00, "Nabil")

print(ba2.info())

ba2.deposit(2)

print(ba2.info())
