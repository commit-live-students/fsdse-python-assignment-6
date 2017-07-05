class Account(object):
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

class Savings(Account):

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        if self.balance - balance < self.minimum_balance():
            print "account minimum balance must be maintained"
        else:
            self.balance = self.balance - balance


    def minimum_balance(self):
        return 1000


class Current(Account):

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        if self.balance - balance -0.1 < self.minimum_balance():
            print "account minimum balance must be maintained"
        else:
            self.balance = self.balance - balance - 0.1

    def minimum_balance(self):
        return 15000
