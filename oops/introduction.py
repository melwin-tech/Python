
# 1. What is OOP?

# Object-Oriented Programming (OOP) is a programming paradigm (a style or way of coding) based on the concept of objects.

# An object is something that has:
# Attributes (data) → e.g., color, size, name
# Behaviors (methods) → e.g., move(), start(), eat()

# In OOP, we group data and the functions that operate on that data together into one logical unit — the class.
# Example (Conceptual):
# Think of a Car:
# Attributes → color, brand, model, speed
# Behaviors → start(), stop(), accelerate(), brake()
# So in OOP:
# Class = Car (blueprint)
# Object = my_car, your_car, etc. (real instances)

# 2. Procedural vs Object-Oriented Programming

# | Aspect              | Procedural Programming          | Object-Oriented Programming                |
# | :------------------ | :------------------------------ | :----------------------------------------- |
# | Focus               | Functions and procedures        | Objects and classes                        |
# | Data                | Data is separate from functions | Data and functions are bundled together    |
# | Example             | `def add(a,b): return a+b`      | `class Calculator: def add(self,a,b): ...` |
# | Reusability         | Harder to extend                | Easier to extend via inheritance           |
# | Real-world Modeling | Limited                         | Very natural                               |

# 3. Why OOP?

# Here are the key advantages of OOP:
# Modularity – code is organized into classes and objects
# Reusability – through inheritance
# Scalability – easy to expand or modify features
# Maintainability – logical grouping of related functionality
# Abstraction – hide unnecessary details
# Encapsulation – protect data from unintended modification

#  4. OOP in Python — Key Concepts (the “4 Pillars”)

# OOP in Python is built around four main principles (memorize these — they’re core to everything you’ll learn later):

# | Pillar            | Meaning                                                | Example                                       |
# | :---------------- | :----------------------------------------------------- | :-------------------------------------------- |
# | **Encapsulation** | Bundling data and functions together                   | A class has both variables and methods        |
# | **Abstraction**   | Hiding internal details, showing only essentials       | Car’s “start” button hides the engine details |
# | **Inheritance**   | Child class inherits features of parent class          | `Dog` inherits from `Animal`                  |
# | **Polymorphism**  | One function behaves differently for different objects | `len()` works for lists, strings, etc.        |
