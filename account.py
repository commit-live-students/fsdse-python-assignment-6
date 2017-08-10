class Account(object):

    def __init__(self, account_num):
        self.balance = 0
        self.account_num = account_num

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        return self.balance


class Savings(Account):

    def __init__(self, account_num):
        super(Savings, self).__init__(account_num)
        self.minimum_balance = 1000

    def withdraw(self, withdraw_amount):
        if (self.balance - withdraw_amount) > self.minimum_balance:
            self.balance = self.balance - withdraw_amount
            return self.balance
        else:
            return False


class Current(Account):

    def __init__(self, account_num):
        super(Current, self).__init__(account_num)
        self.minimum_balance = 15000

    def withdraw(self, withdraw_amount):
        if (self.balance - withdraw_amount) > self.minimum_balance:
            self.balance = self.balance - (withdraw_amount + 0.1)
            return self.balance
        else:
            return False
