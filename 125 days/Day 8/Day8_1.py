 
#Implement a Python class representing a simple bank account with deposit and withdrawal methods
 
class BankAccount:
 
    def __init__(self, initial_balance=0):
 
        self.balance = initial_balance
 
 
    def deposit(self, amount):
 
        self.balance += amount
 
 
    def withdraw(self, amount):
 
        if amount <= self.balance:
 
            self.balance -= amount
 
        else:
 
            print("Insufficient funds!")
 
 
# Creating an instance of a bank account
 
my_account = BankAccount()
 
 
# Depositing money into the account
 
my_account.deposit(100)
 
 
# Withdrawing money from the account
 
my_account.withdraw(50)
 
 
# Checking the account balance
 
print("Account balance:", my_account.balance)
 
