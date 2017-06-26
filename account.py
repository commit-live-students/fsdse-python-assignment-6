class account(object):
    balance = 0
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < 1000:
            print ("Minimum balance of 1000 required")
        else:
            self.balance = self.balance - amount

class Savings(account):
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

class Current(account):
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
    def withdraw(self, amount):
        if self.balance >= 15000:
            self.balance = self.balance - (amount+(0.1*amount))
        else:
            print("Minimum balance of 15000 required for withdrawal from current account")
