
# A function is a block of code that performs a specific task.
# It runs only when it is called, and it helps make programs modular, reusable, and cleaner.

# Functions in Python can be broadly divided into two categories:
# Built-in Functions
# User-defined Functions

# 1 Built-in Functions
# These are already defined in Python.
# You can use them anytime — no need to define them yourself.
# Examples:
# print(), input(), len(), max(), min(), type()

# 2. User-defined Functions
# These are created by the programmer to perform specific tasks.
# Example:
def add(a, b):
    return a + b
result = add(10, 5)
print("Sum:", result)

# Functions based on parameter and return

# 1. no parameter with no return
def greet():
    print("Hello world")
greet()

# 2. no parameter with return
def greet():
    return "Hello world"
my_greet = greet()
print(my_greet)

# 3. with parameter and no return
def sum_of_two(a,b):
    print("The sum is : ",a+b)
sum_of_two(2,4)

# 4. with parameter and with return
def sum_of_two(a,b):
    return a+b
sum_of_two = sum_of_two(2,4)
print("The sum is : ",sum_of_two)

# Functions based on aruguments

# 1. Positional arguments
# Positional arguments are passed to a function in the same order as the parameters are defined. The position of each argument matters.
def student(name, age):
    print("name : ",name,", age : ",age)
student("Melwin",20)

# 2. Keywords arguments
# Keyword arguments are passed using the parameter name. The order of arguments does not matter because they are matched by name.
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=20, name="Alice")

# 3. Default arguments
# Default arguments have predefined values in the function definition.
# If no value is provided during the call, the default value is used.
def greet(name="User"):
    print("Hello,", name)
greet()
greet("Ravi")

# 4. Variable-length arguments (*args)
# *args allows a function to accept any number of positional arguments.
# All values are collected into a tuple.
def add_numbers(*args):
    print("Arguments:", args)
    print("Sum:", sum(args))
add_numbers(2, 4, 6)
add_numbers(1, 2, 3, 4, 5)

# 5. Variable-length keyword arguments (*kwargs)
# **kwargs allows a function to accept any number of keyword arguments.
# All key-value pairs are collected into a dictionary.
def show_details(**kwargs):
    print("Details:", kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)
show_details(name="Alice", age=22, city="Delhi")

# Some special types of function
# A lambda function is a small, one-line, unnamed function.
square = lambda x: x * x
print(square(5))  

# Some important concepts related to variable
# global and local Variables
# Local variable → defined inside a function; accessible only there.
# Global variable → defined outside all functions; accessible everywhere.
x = 10   # global
def show():
    x = 5  # local
    print("Local x:", x)
show()
print("Global x:", x)