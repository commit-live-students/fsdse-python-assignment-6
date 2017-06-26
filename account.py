class Account(object):
   balance = 0
   def __init__(self, acctNumber):
      self.acctNumber = acctNumber

   def __str__(self):
      return "Account number: " + str(self.acctNumber) + "\n" + \
             "Balance: " + str(self.balance)

   def deposit(self, amount):
      self.balance += amount

class Current(Account):
   def __init__(self, acctNumber):
      Account.__init__(self, acctNumber)

   def __str__(self):
      retStr = "Account type: Current\n"
      retStr += Account.__str__(self)
      return retStr

   def withdraw(self, amount):
      if amount > self.balance or self.balance < 15000:
         print("Insufficient funds.")
      else:
         self.balance = self.balance - amount - (amount * 0.1)

class Savings(Account):
   def __init__(self, acctNumber):
      Account.__init__(self, acctNumber)

   def __str__(self):
      retStr = "Account type: Savings\n"
      retStr += Account.__str__(self)
      return retStr

   def withdraw(self, amount):
      if amount > self.balance or self.balance < 1000:
         print("Insufficient funds.")
      else:
         self.balance = self.balance - amount
