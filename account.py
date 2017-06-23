class Account(object):
    def __init__(self,n):
        self.balance=0.0
        self.acc_no = n
    def get_acc_no(self):
        return self.acc_no

    def deposit(self,amt):
        if amt<=0:
            print("Can't have negative or zero deposits")
        else:
            self.balance = self.balance+amt

    def withdraw(self,amt):
        if amt<=0:
            print("Can't have negative or zero witdrawals")
        else:
            self.balance = self.balance-amt
        return self.balance

class Savings(Account):
    def __init__(self,n):
        super(Savings,self).__init__(n)

class Current(Account):
    def __init__(self,n):
        super(Current,self).__init__(n)
    def withdraw(self,amt):
        if amt<=0:
            print("Can't have negative or zero witdrawals")
        else:
            self.balance = self.balance-(amt+amt*0.1)
        return self.balance





c = Current(1234)
print(c.deposit(20000))
print(c.withdraw(1))
print(c.balance)
