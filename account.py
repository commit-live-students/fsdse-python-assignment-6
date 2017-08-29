class Account:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print('Your balance after the deposit is %.2f' %self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds for this transaction')
        else:
            self.amount = amount
            self.balance -= (amount)
            print('Your balance after the withdrawal is %.2f' %self.balance)
class Savings(Account):
    def __init__(self, acc_num):
        Account.__init__(self, balance = 0)
        self.acc_num = acc_num

class Current(Account):
    def __init__(self, acc_num):
        Account.__init__(self, balance = 0)
        self.acc_num = acc_num

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds for this transaction')
        else:
            self.amount = amount
            self.balance -= (amount+0.1)
            print('Your balance after the withdrawal is %.2f' %self.balance)
