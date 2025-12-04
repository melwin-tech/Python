
# Definition:
# "Polymorphism" means "many forms".
# It allows the same method or operator to behave differently 
# depending on the object or data type it is used with.
# Example: The + operator adds numbers but concatenates strings.


# 1️. Polymorphism with Built-in Functions and Operators
print("----- Polymorphism with Built-in Functions -----")
print(len("Hello World"))      # works on string → counts characters
print(len([1, 2, 3, 4, 5]))    # works on list → counts elements
print(10 + 5)                  # numeric addition
print("Hello " + "Python")     # string concatenation


# 2️. Polymorphism with Functions and Objects
# When the same function works for different classes
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

def animal_sound(animal):
    # Function behaves differently depending on which object is passed
    print(animal.sound())

print("\n----- Polymorphism with Functions and Objects -----")
dog = Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)


# 3️. Polymorphism using Inheritance and Method Overriding
# Method Overriding means: Child class redefines a method from the Parent class
class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def start(self):  # Overriding parent method
        print("Starting the car with a key...")

class ElectricCar(Vehicle):
    def start(self):  # Overriding differently
        print("Starting the electric car silently...")

print("\n----- Method Overriding Example -----")
v = Vehicle()
c = Car()
e = ElectricCar()

v.start()
c.start()
e.start()


# 4️. Polymorphism using Abstract Classes (Runtime Polymorphism)
# Using abc (Abstract Base Class) module
# Abstract classes are templates that force child classes to implement certain methods
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

print("\n----- Abstract Class and Runtime Polymorphism -----")
shapes = [Rectangle(10, 20), Circle(5)]

for shape in shapes:
    print(f"Area: {shape.area()}")


# 5️. Polymorphism with Constructors
# In Python, we can achieve constructor overloading using default arguments
class Student:
    def __init__(self, name=None, marks=None):
        if name is not None and marks is not None:
            self.name = name
            self.marks = marks
        elif name is not None:
            self.name = name
            self.marks = 0
        else:
            self.name = "Unknown"
            self.marks = 0

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

print("\n----- Constructor Polymorphism Example -----")
s1 = Student("Rahul", 85)
s2 = Student("Amit")
s3 = Student()
s1.display()
s2.display()
s3.display()


# 6️. Polymorphism with Method Overloading (Pythonic Way)
# Note: Python doesn’t support true method overloading like Java or C++
# But we can simulate it using default parameters or *args
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

print("\n----- Method Overloading Example -----")
calc = Calculator()
print("Sum of 2 numbers:", calc.add(10, 20))
print("Sum of 3 numbers:", calc.add(10, 20, 30))
print("Sum of 1 number :", calc.add(5))


# 7. Operator Overloading (Compile-time Polymorphism)
# We can redefine the behavior of operators for user-defined classes
# using special methods like __add__, __sub__, __mul__, etc.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overload + operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

print("\n----- Operator Overloading Example -----")
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # calls __add__()
print("Result of addition:", p3)

# Summary of Polymorphism Types
'''
1. Polymorphism with Built-in Functions  → same function, different data types
2. Polymorphism with Functions and Objects → same function works for different objects
3. Method Overriding (Inheritance)        → same method, different behavior in child
4. Abstract Classes (Runtime Polymorphism)→ ensures subclasses implement common methods
5. Constructor Polymorphism               → same constructor behaves differently
6. Method Overloading                     → same method name, different arguments
7. Operator Overloading                   → redefining operators for custom classes
'''

print("\nAll types of Polymorphism demonstrated successfully!")
