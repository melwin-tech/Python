
# Abstraction means hiding complex internal details and showing only what is necessary.
# It focuses on *what an object does* instead of *how it does it*.
# Example: When you use a phone, you tap buttons — you don’t need to know how the hardware works internally.
# We achieve abstraction in Python using:
# 1. Abstract Classes and Methods (abc module)
# 2. Encapsulation (private and protected members)


# 1. Abstraction using Abstract Classes

from abc import ABC, abstractmethod

# Abstract class is a blueprint for other classes
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class - must implement all abstract methods
class Car(Vehicle):
    def start(self):
        print("Car engine started with a key.")

    def stop(self):
        print("Car stopped safely.")

class Bike(Vehicle):
    def start(self):
        print("Bike started using self start button.")

    def stop(self):
        print("Bike stopped with hand brakes.")

print("Abstraction Example 1 - Using Abstract Classes")
car = Car()
bike = Bike()
car.start()
car.stop()
bike.start()
bike.stop()


# 2. Abstraction using Encapsulation (private and protected members)

# Here we hide the data and provide only controlled access through methods.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable (hidden)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Invalid or insufficient funds.")

    # This is a public method that allows controlled access to balance
    def get_balance(self):
        print(f"Current balance for {self.owner} is: ₹{self.__balance}")

print("\nAbstraction Example 2 - Using Encapsulation")
account = BankAccount("Rahul", 10000)
account.deposit(5000)
account.withdraw(3000)
account.get_balance()

# Trying to access private variable directly (will fail)
# print(account.__balance)  # AttributeError

# Correct way to access: through a method
account.get_balance()


# 3. Real-life Example: Payment System

# Abstract class defines the structure
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Different classes provide their own implementations
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI method.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} in Cash.")

print("\nAbstraction Example 3 - Real-life Payment System")
payments = [CreditCardPayment(), UpiPayment(), CashPayment()]
for method in payments:
    method.pay(1500)


# Summary of Abstraction:
# 1. Abstract classes define what to do (method name)
# 2. Child classes define how to do it (implementation)
# 3. Hides internal details using private variables and methods
# 4. Achieved in Python through abc module and encapsulation


print("\n All concepts of Abstraction demonstrated successfully!")
