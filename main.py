class BankAccount:
def int  (self.account_number,account_holders_name,initial_balance==0):
  self.__account_number=account_number
  self.__account_holder_name=account_holder_name
  self.__account_balance=initial_balance
 def deposite(self.amount):
   if amount>0:
     self.__account_balance+=amount
     print("deposit rs{} new balance:rs{}.format(amount,self.__account_balance"))
   else:
     print("invalid deposit amount.please deposit a positive amount")
     def withdraw(self.amount):
       if amount>0 and amount<=self.__account_balance:
         self.__account_balance= amount
         print("withdraw rs{} new balance:rs{}"format(amount,self.__account_balance))
       else:
         print("invalid withdrawal amount or insufficient balance")
         def display_balance(self):
           print("account balance for{}(account#{}.rs{}".format(self.__account_holder_name,self.___accound_number,self.__account_balance))
 #create an instance of the BankAccount class
  account=BankAccount(account_number="123456789",account_holder_name="kayal", initial_balance=2000.0)
         