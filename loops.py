
# A loop is a programming structure that repeats a block of code multiple times — until a condition is met (or for every item in a sequence).
# Python has two main types of loops:
# for loop — used to iterate over a sequence (list, tuple, dict, set, string, etc.).
# while loop — used to repeat code while a condition is True.

# 1) For loop
# a) for loop with lists
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# you can also use it with range () in order to traverse the list
for i in range(len(fruits)):
    print(i, fruits[i])

# b) for loop with tuple
numbers = (10, 20, 30)
for num in numbers:
    print(num)

# c) for loop with dictionary
student = {"name": "Alice", "age": 21, "grade": "A"}
for key in student:
    print(key)            # loop through keys

for value in student.values():
    print(value)          # loop through values

for keys,values in student.items():
    print("Key:",key, "and value : ",values)    # loop through key value

# d) for loop with set
colors = {"red", "green", "blue"}
for color in colors:
    print(color)

# 2. While loop
# ex:
i = 1
while i <= 10 :
    print(i, ": Hello World")
    i = i + 1

# 3. some special control statements
# a) break
for i in range(5):
    if i == 3:
        break        # stops the loop
    print(i)

i = 0
while i < 5:
    if i == 3:
        break       # stops the loop
    print(i)
    i += 1

# b) continue
for i in range(5):
    if i == 2:
        continue     # skips this iteration
    print(i)

i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)

# c) else
for i in range(3):
    print(i)
else:
    print("Loop finished!")

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop ended normally")

# 4) pass
for i in range(5):
    pass

i=0
while i in range(5):
    i+=1
    pass


