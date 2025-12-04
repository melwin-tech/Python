
# 1. What is Encapsulation?

# Encapsulation means wrapping up data and methods into a single unit (class) and controlling access to that data.
# In simple words:
# “Encapsulation is like putting your car’s engine under the hood — you can drive the car, but you can’t directly mess with the engine parts.”
# So, in programming:
# Your class hides its internal data (attributes).
# Other parts of your code can only interact through methods (controlled access).

# 2. Why Encapsulation is Important

# Protects data from accidental modification
# Prevents misuse of internal details
# Helps maintain cleaner, safer, and more maintainable code
# Allows controlled access (read-only, write-only, etc.)

# 3. Types of Access Modifiers in Python

# In some languages (like Java or C++), you have public, protected, and private keywords.
# Python doesn’t strictly enforce these — but uses naming conventions to indicate intent.
# | Type          | Syntax        | Meaning                                                  |
# | :------------ | :------------ | :------------------------------------------------------- |
# | Public    | `self.name`   | Accessible everywhere                                    |
# | Protected | `self._name`  | Should not be accessed directly (but possible)           |
# | Private   | `self.__name` | Name-mangled — not directly accessible outside the class |

#  1. Public
# Everything in a class is public by default.
# Attributes are accessible from everywhere like within the class and outside the class

class Car:
    def __init__(self, name, price):
        self.name = name     # public attribute
        self.price = price   # public attribute

    def display(self):
        print(f"Car: {self.name}, Price: ₹{self.price}")

car1 = Car("BMW", 5000000)
car1.display()

# Accessible from outside
print(car1.name)
print(car1.price)

#  2. Protected 
# A protected member is a convention — you’re saying:
# “This variable is for internal use. Please don’t access it directly.”
# It’s still accessible, but developers are expected not to.
class Car:
    def __init__(self, name, price):
        self._price = price   # protected attribute
        self.name = name

    def show(self):
        print(f"Car: {self.name}, Price: ₹{self._price}")

car1 = Car("Audi", 6000000)
car1.show()

# Can still be accessed, but not recommended
print(car1._price)

# 3. Private
# Private members are truly hidden.
# They can’t be accessed directly from outside the class.
class Car:
    def __init__(self, name, price):
        self.__price = price   # private attribute
        self.name = name

    def show(self):
        print(f"Car: {self.name}, Price: ₹{self.__price}")

car1 = Car("Mercedes", 8000000)
car1.show()

# Trying to access directly -> Error!
# print(car1.__price)   AttributeError

# But you can access indirectly via name mangling (not recommended)
print(car1._Car__price)

#  some special concepts

# 1. Controlling Access Using Getters and Setters
# We often don’t want users to directly modify private data —
# so we use getter and setter methods to control access.
class Car:
    def __init__(self, name, price):
        self.__price = price
        self.name = name

    # Getter method — allows read access
    def get_price(self):
        return self.__price

    # Setter method — allows controlled write access
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

car1 = Car("Tesla", 9000000)
# Access price safely
print(car1.get_price())
# Modify price safely
car1.set_price(10000000)
print(car1.get_price())
# Try invalid change
car1.set_price(-200)

# 2. Property Decorators
class Car:
    def __init__(self, name, price):
        self.__price = price
        self.name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

car1 = Car("Tesla", 9000000)
# Access price safely
print(car1.price)
# Modify price safely
car1.price = 100000000
print(car1.price)
# Try invalid change
car1.price = -120

# Small example of bank application using the concept of encapsulation
class Bank:
    def __init__(self,Account_name,balance=0):
        self.Account_name = Account_name
        self.__balance = balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print("Amount Deposited succesfully")
        else:
            print("Deposited amount must be positive")
    
    def withdraw(self,amount):
        if amount > self.__balance :
            print("Insufficient Amount in the balance")
        elif amount>0:
            self.__balance -= amount
            print("Amount Withdrawn succesfully")
        else:
            print("invalid withdrawal amount")


    def display(self):
        print("Account holder name : ",self.Account_name)
        print("Account holder balance : ",self.__balance)

acc_1 = Bank("Melwin Dsouza",50000)

acc_1.display()

acc_1.deposit(-1000)
acc_1.deposit(1000)
acc_1.display()

acc_1.withdraw(-6789)
acc_1.withdraw(60000)
acc_1.withdraw(1000)
acc_1.display()

