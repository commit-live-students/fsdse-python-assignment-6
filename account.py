class Account:
    balance = 0
    def deposit(self,bal):
        self.balance += bal
    def withdraw(self,bal):
        if self.balance > bal:
            self.balance -= bal
class Savings(Account):
    def __init__(self,name):
        self.name = name

class Current(Account):
    def __init__(self,name):
        self.name = name
    def deposit(self,bal):
        if bal > 15000:
            self.balance += bal
    def withdraw(self,bal):
        if self.balance > bal:
            self.balance = self.balance - bal - bal*0.1
