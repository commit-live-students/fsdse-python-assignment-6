class Account(object):
    def __init__(self, account_no):
       self.account_no = account_no
       self.balance = 0

    def deposit(self, money):
       self.balance += money

    def withdraw(self, money):
       if self.balance > 1000 :
           self.balance -= money
       else:
           raise Exception("Cannot withdraw")

class Savings(Account):
    pass

class Current(Account):
   def withdraw(self, money):
       if(self.balance > 15000):
           money += 0.1*money
           self.balance -= money
       else:
           raise Exception("Cannot withdraw")
