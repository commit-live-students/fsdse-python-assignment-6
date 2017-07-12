# Manage Saving and Current account for user
# clive open fsdse-python-assignment-6

class Account(object):
    balance = 0
    def __init__(self, acc_number):
        self.acc_number = acc_number


    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

class Savings(Account):
    def __init__(self, acc_number):
        self.acc_number = acc_number

class Current(Account):
    def __init__(self, acc_number):
        self.acc_number = acc_number

    def withdraw(self, amount):
            self.balance = self.balance - amount - 0.1*amount
