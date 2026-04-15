# ================================================
# DAY 6 - Object Oriented Programming (OOP) Basics
# ================================================
# Goal: Learn Classes, Objects, Attributes and Methods

print("=== Day 6 - OOP Basics Started ===\n")

# 1. Simple Class
class Person:
    """This is a Person class"""
    
    # Constructor (runs when we create a new object)
    def __init__(self, name, age, city="Regina"):
        self.name = name          # Attribute
        self.age = age            # Attribute
        self.city = city          # Attribute
        self.is_active = True     # Default attribute
    
    # Method (function inside class)
    def introduce(self):
        print(f"Hi, my name is {self.name}.")
        print(f"I am {self.age} years old and I live in {self.city}.")
    
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! Now you are {self.age} years old.")
    
    def deactivate(self):
        self.is_active = False
        print(f"{self.name} account has been deactivated.")

# 2. Creating Objects (Instances)
print("1. Creating Objects:")

person1 = Person("JAY", 25, "Regina")
person2 = Person("Sarah", 28, "Saskatoon")

person1.introduce()
print()
person2.introduce()
print()

# 3. Using Methods
print("2. Using Methods:")
person1.have_birthday()
person2.have_birthday()
print()

# 4. Accessing and Modifying Attributes
print("3. Attributes:")
print(f"{person1.name} lives in {person1.city}")
print(f"{person2.name} is active: {person2.is_active}")

person2.deactivate()
print(f"After deactivation - {person2.name} is active: {person2.is_active}")
print()

# 5. Mini Project - Simple Bank Account Class
print("4. Mini Project: Bank Account Class")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("❌ Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrew ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("❌ Insufficient funds!")
        else:
            print("❌ Withdrawal amount must be positive.")
    
    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

# Using the Bank Account
account = BankAccount("JAY", 500)
account.show_balance()
account.deposit(300)
account.withdraw(150)
account.withdraw(700)   # This should fail
account.show_balance()

print("\n=== Day 6 Completed Successfully! ===")
print("You now understand the basics of Classes and Objects!")