class BankAccount(object):
    __secretKey = 1234
    defaultAccountNumber = 10

    def __init__(self, name, balance = 5):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccountNumber
        BankAccount.defaultAccountNumber += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough money!")
        else:
            self.balance -= amount

    def getBalance(self):
        return self.balance

    def ret(self):
        return self.__secretKey

if __name__ == '__main__':
    print("\n### BANK OF XYZ ###")
    myObj = BankAccount("RGB", 50)
    myObj.deposit(100)
    print(myObj.getBalance())
    myObj.withdraw(25)
    print(myObj.getBalance())
    print("\nThe secret key is:", myObj.ret())
