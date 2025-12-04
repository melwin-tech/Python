
# List is sequenece data type which is ordered, muteable, allow duplicate values of the collections of the items
# ex : list_1 = [1,"Meliwn",3.14,] etc

# 1. Creation of the list
# a) by directly
fruits = ["Mango", "Watermelon", "Banana", "Kiwi","Orange","Apple"]
print(fruits)
# b) by type-casting
text = "Hello"
text_1 = list(text)
print(text_1)

# 2. Acessing the lists elements (indexing and slicing of the lists)
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

# 3. Modifying the lists  
# a) updating the elements
fruits[1] = "blueberry"
print(fruits)  
# b) Adding elements
fruits.append("Peru")   # Add at end
print(fruits)
fruits.insert(1, "Dry_fruits") # Add at index 1
print(fruits)
# c) Removing elements 
fruits.remove("Apple")  # Remove by value
print(fruits)
fruits.pop(2)           # Remove by index
print(fruits)
fruits.clear()          # Remove all items
print(fruits)

# 4. Some other methods in the lists
# a) Sorting (both sort(),sorted())
mylists = [12,4,34,45,7,89,100,34,56,21]
print(mylists)
print("Asscending order sorting : ",sorted(mylists))
print("Desscending order sorting : ",sorted(mylists, reverse= True))
# b) index and count
numbers = [10, 20, 30, 40, 20, 50]
print(numbers)
print(numbers.index(20))         # First occurrence of 20
print(numbers.index(20, 2))      # Search for 20 starting from index 2
print(numbers.count(20))  # How many times 20 appears
print(numbers.count(10))  # How many times 10 appears
print(numbers.count(99))  # How many times 99 appears (0 if not found)
# c) copy vs reference
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] — both changed (same reference)
# To avoid this:
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3] — separate lists
