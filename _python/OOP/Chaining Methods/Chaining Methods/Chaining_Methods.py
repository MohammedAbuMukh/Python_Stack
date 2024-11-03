class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self



user1 = User("Guido van Rossum", 150)
user2 = User("Linus Torvalds", 200)
user3 = User("Grace Hopper", 300)


user1.make_deposit(50).make_deposit(30).make_deposit(20).make_withdrawal(100).display_user_balance()

user2.make_deposit(100).make_deposit(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

user3.make_deposit(200).make_withdrawal(100).make_withdrawal(50).make_withdrawal(100).display_user_balance()

