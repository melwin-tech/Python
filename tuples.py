
#  Tuple is sequenece data type which is ordered, immuteable, allow duplicate values of the collections of the items
# ex : tuple_1 = (1,"Melwin",3.14) etc ...

# 1. Creation of tuple
# a) by directly
fruits = ("Mango", "Watermelon", "Banana", "Kiwi","Orange","Apple")
print(fruits)
print(type(fruits))
# b) by type-casting
text = "Hello"
text_1 = tuple(text)
print(text_1)
print(type(text_1))

# 2. Acessing the lists elements (indexing and slicing of the tuples)
print(fruits)
print("Starting elements : ",fruits[0])
print("Ending  : ",fruits[-1])
print("At index 4 : ",fruits[4])
print("Staring three elements : ",fruits[:3])
print("Ending three elements : ",fruits[-3:])
print("Excluding start three elements : ",fruits[3:])
print("Excluding end three elements : ",fruits[:-3])
print("From index 3 to 6 : ",fruits[3:7])
print("Reverse the list : ",fruits[::-1])

# 3. Modifying the tuple
# You cannot update, add, or remove items once created.
# fruits = ("apple", "banana", "cherry")
# fruits[1] = "kiwi"   -> TypeError: 'tuple' object does not support item assignment
#  So the solution is that :
'''
If you want to modify a tuple, you must:
Convert it to a list
Modify the list
Convert it back
'''
fruits = ("apple", "banana", "cherry") # tuple fruits
print(fruits)
print(type(fruits))
temp = list(fruits) # type caste it to list temp
print(temp)
print(type(temp))
temp.append("mango") # applying the modifications 
print(temp)
print(type(temp))
fruits = tuple(temp) # type caste back to tuple
print(fruits)
print(type(fruits))
# you can use all the lists methods once the tuple is converted to the list and do changes and then convert it back to the tuple .

# 4. Some important methods in the tuple
# a) Sorting Tuples (only sorted() works )
mytuple = (12, 4, 34, 45, 7, 89, 100, 34, 56, 21)
print("Original tuple:", mytuple)
# Ascending order sorting
print("Ascending order sorting :", sorted(mytuple))
# Descending order sorting
print("Descending order sorting :", sorted(mytuple, reverse=True))
# b) index and count
numbers = (10, 20, 30, 40, 20, 50)
print(numbers)
print(numbers.index(20))         # First occurrence of 20
print(numbers.index(20, 2))      # Search for 20 starting from index 2
print(numbers.count(20))  # How many times 20 appears
print(numbers.count(10))  # How many times 10 appears
print(numbers.count(99))  # How many times 99 appears (0 if not found)
