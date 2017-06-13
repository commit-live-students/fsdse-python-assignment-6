class Account(object):
   balance = 0
   def __init__(self, accNum):
      self.accNum = accNum

   def __str__(self):
      return "Account number: " + str(self.accNum) + "\n" + \
             "balance: " + str(self.balance)

   def deposit(self, amt):
      self.balance += amt

class Current(Account):
   def __init__(self, accNum):
      Account.__init__(self, accNum)

   def __str__(self):
      retStr = "Account type: Current\n"
      retStr += Account.__str__(self)
      return retStr

   def withdraw(self, amt):
      if amt > self.balance or self.balance < 15000:
         print("Insufficient minimun balance.")
      else:
         self.balance = self.balance - amt - (amt * 0.1)

class Savings(Account):
   def __init__(self, accNum):
      Account.__init__(self, accNum)

   def __str__(self):
      retStr = "Account type - Savings\n"
      retStr += Account.__str__(self)
      return retStr

   def withdraw(self, amt):
      if amt > self.balance or self.balance < 1000:
         print("Insufficient minimun balance.")
      else:
         self.balance = self.balance - amt
