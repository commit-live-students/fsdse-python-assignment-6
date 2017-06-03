class account(object):

    def __init__(self, accnum):
        self.accnum = accnum
        self.balance = 0

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance = self.balance - amt


class Savings(account):

    def __init__(self, accnum):
        self.accnum = accnum
        self.balance = 0


class Current(account):

    def __init__(self, accnum):
        self.accnum = accnum
        self.balance = 0

    def withdraw(self, amt):
        self.balance = self.balance - (amt+(0.1*amt))
