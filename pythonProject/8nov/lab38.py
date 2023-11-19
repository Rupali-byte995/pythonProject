class BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
    def _withdraw(self,amount):
        self.balance=self.balance-amount
    def __showBalance(self):
       print("Your balance is ",self.balance)
    def authenticate(self,isAuth):
        if isAuth:
            self.__showBalance()
        else:
            print("You are not authenticated")
jpmorgan=BankAccount()
a=int(input("Enter amount"))
b=int(input("Enter amount to withdraw"))
jpmorgan.deposit(a)
jpmorgan._withdraw(b)
jpmorgan.authenticate(True)
