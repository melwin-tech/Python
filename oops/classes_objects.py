
# Class is a blueprint of the object
# Object is an instance of the class

# 1. creating a class and object
'''
syntax:
class ClassName:
    # class body
    # attributes + methods

my = ClassName()    -> create an object

'''

class Car:

    country = "India"  # Global attribute

    # In simple words:
    # __init__() is a special method that runs automatically whenever you create a new object from a class.
    # It’s called the constructor — its job is to set up (initialize) the object with data (like name, color, price).
    # Think of it like:
    # When you buy a new car, the company builds it and installs your chosen features (color, model, engine type).
    # __init__() does the same thing — it builds your object and gives it the data you provide
    # self means "this particular object".
    # It’s how the class keeps track of which object it’s talking about.
    # When you create multiple objects, self helps the class know which one to use.

    def __init__(self,name,color,price):    # constructor in python
        self.name = name
        self.color = color
        self.price = price

    # Method in the class   
    def start(self):       
        print(self.name , ": This car is starting")
    
    def stop(self):
        print(self.name , ": This car is stoping")
       
car_1 = Car("Bmw","Black","500000")  # creation of the object in the class
print(car_1.name)               # using the objects attributes for some purpose
print(car_1.color)
print(car_1.price)
print(car_1.country)
car_1.start()                   # using the methods for some purpose
car_1.stop()

# Every objects keeps its own data
car_2 = Car("Audi", "White", "600000")
print(car_2.name)               
print(car_2.color)
print(car_2.price)
print(car_2.country)
car_2.start()                   
car_2.stop()

# class variable is shared 
print(Car.country)   # Access via class name
# Change the class variable using class name
Car.country = "Germany"
print(car_1.country)  # Both car_1 and car_2 will now show Germany
print(car_2.country)

