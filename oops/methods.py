
# 1. What are Methods?

# A method is simply a function defined inside a class.
# It defines the behavior or actions that an object can perform.
# In simple words:
# Attributes → describe what an object is
# Methods → describe what an object does

# 2. Types of Methods in python
# Python supports 3 types of methods:

# | Type                | Decorator       | First Parameter | Belongs To        | Access                         |
# | :------------------ | :-------------- | :-------------- | :---------------- | :----------------------------- |
# | **Instance Method** | *(none)*        | `self`          | Individual object | Accesses instance + class data |
# | **Class Method**    | `@classmethod`  | `cls`           | Entire class      | Accesses class-level data      |
# | **Static Method**   | `@staticmethod` | none            | Neither           | Independent utility logic      |

# Lets see one by one 

#  1. Instance Methods
# Definition:
# Instance methods work on individual objects.
# They can access and modify instance variables.
class Car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    # Instance method
    def show_details(self):
        print(f"Car: {self.name}, Color: {self.color}, Price: {self.price}")

car1 = Car("BMW", "Black", 500000)
car1.show_details()

# 2. Class Method
# Definition:
# Class methods work on the class itself, not on individual objects.
# They use the @classmethod decorator and have cls as their first parameter.
# You can use them to access or modify class variables (shared across all objects)
class Cars:
    country = "India"   # class variable

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country
        print("Country changed to:", cls.country)

Cars.change_country("Germany")   # Accessing via class name

# 3. Static method

# Definition:
# Static methods are independent utility functions inside a class.
# They don’t need access to either instance (self) or class (cls) data.
# They’re created using the @staticmethod decorator.

class Carss:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    
    @staticmethod
    def company_info():
        print("All cars are made under Car Manufacturing Pvt. Ltd.")

