
# Inheritance allows one class (child) to use properties and methods of another class (parent) — helping with code reusability and structure.

# 1️. Single Inheritance
# One child class inherits from one parent class
class Parent:
    country = "India"
    def feature_parent(self):
        print("Feature from Parent class")

class Child(Parent):  # Child inherits from Parent
    def feature_child(self):
        print("Feature from Child class")

print("----- Single Inheritance -----")
obj1 = Child()
obj1.feature_parent()
obj1.feature_child()
print(obj1.country)



# 2️. Multilevel Inheritance
# When a class inherits from another child class
# Example: Grandparent → Parent → Child
class GrandParent:
    def feature_grandparent(self):
        print("Feature from GrandParent class")

class Parent2(GrandParent):
    country = "India"
    def feature_parent2(self):
        print("Feature from Parent class")

class Child2(Parent2):
    def feature_child2(self):
        print("Feature from Child class")

print("\n----- Multilevel Inheritance -----")
obj2 = Child2()
obj2.feature_grandparent()
obj2.feature_parent2()
obj2.feature_child2()
print(obj1.country)

# 3️. Multiple Inheritance
# When a class inherits from more than one parent
# Example: Child inherits from both Father and Mother
class Father:
    def feature_father(self):
        print("Feature from Father")

class Mother:
    def feature_mother(self):
        print("Feature from Mother")

class Child3(Father, Mother):  # inherits from both
    def feature_child3(self):
        print("Feature from Child class (Multiple Inheritance)")

print("\n----- Multiple Inheritance -----")
obj3 = Child3()
obj3.feature_father()
obj3.feature_mother()
obj3.feature_child3()


# 4️. Hierarchical Inheritance
# Multiple child classes inherit from the same parent
# Example: Parent → ChildA, ChildB
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

print("\n----- Hierarchical Inheritance -----")
dog = Dog()
cat = Cat()
dog.sound()
dog.bark()
cat.sound()
cat.meow()


# 5. Hybrid Inheritance
# Combination of multiple inheritance types
# Example: A base class is inherited by multiple classes,
# and one of those child classes is also inherited by another class.
class A:
    def feature_a(self):
        print("Feature from class A")

class B(A):
    def feature_b(self):
        print("Feature from class B")

class C(A):
    def feature_c(self):
        print("Feature from class C")

class D(B, C):  # D inherits from both B and C (Hybrid)
    def feature_d(self):
        print("Feature from class D")

print("\n----- Hybrid Inheritance -----")
obj4 = D()
obj4.feature_a()  # from A
obj4.feature_b()  # from B
obj4.feature_c()  # from C
obj4.feature_d()  # from D


# Extra Example — Using super() in inheritance
# super() is used to call the parent class constructor or method inside the child class

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"Vehicle brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # calling parent constructor
        self.model = model

    def info(self):
        super().info()  # calling parent method
        print(f"Car model: {self.model}")

print("\n----- Using super() Example -----")
car1 = Car("Tesla", "Model S")
car1.info()


# Summary of Inheritance Types
'''
1. Single Inheritance      → One child inherits from one parent
2. Multilevel Inheritance  → Grandparent → Parent → Child
3. Multiple Inheritance    → Child inherits from multiple parents
4. Hierarchical Inheritance→ One parent, multiple children
5. Hybrid Inheritance      → Combination of multiple types
'''

print("\n All inheritance types demonstrated successfully!")
