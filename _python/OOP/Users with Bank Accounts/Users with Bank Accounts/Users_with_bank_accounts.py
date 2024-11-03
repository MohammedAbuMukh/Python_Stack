class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance +=amount
        return self
    
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self    
        
        
    def display_account_info(self):
         print(f"Balance: ${self.balance}")
         return self  
        
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self  
    

class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  

    def add_account(self, account_name, int_rate=0.01, balance=0):
       
        self.accounts[account_name] = BankAccount(int_rate, balance)

    def make_deposit(self, amount, account_name):
       
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"Account '{account_name}' not found.")
        return self 

    def make_withdrawal(self, amount, account_name):
        
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"Account '{account_name}' not found.")
        return self  

    def display_user_balance(self, account_name):
      
        if account_name in self.accounts:
            print(f"{self.name}'s {account_name} account balance: ${self.accounts[account_name].balance}")
        else:
            print(f"Account '{account_name}' not found.")
        return self 



user = User("Alice")
user.add_account("savings", int_rate=0.02, balance=100)
user.add_account("checking", int_rate=0.01, balance=50)


user.make_deposit(200, "savings").make_withdrawal(50, "checking").display_user_balance("savings")
user.display_user_balance("checking")
