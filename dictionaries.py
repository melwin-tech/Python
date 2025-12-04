
# Dictionaries is mapping data type which collection of key-value pairs. 
# It is unordered(indexed with key not by position), mutable, duplicates : only value are allowed not the keys.
'''
ex : mydict = {
    "Name":"Melwin,
    "Roll_no":20,
    "Department":"Computer Enginnering"
}
'''

# 1. Creation of dictionaries
# a) by direectly
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
print(student)
print(type(student))
# b) using dict constructor
person = dict(name="John", age=25, city="London")
print(person)
print(type(person))

# 2. Accessing the elements of dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
print(student)
print(type(student))
print(student.keys())    # Return a set-like object providing a view on the dict's keys.
print(student.values())  # Return a set-like object providing a view on the dict's values.
print(student.items())   # Return a set-like object providing a view on the dict's (key,value) pairs.
print(student["age"])    # by means of key you access the value of that key
print(student.get("course"))  # Python ( get() is used to avoid the errors )
print(student.get("grade", "N/A"))  # returns 'N/A' if key not found

# 3. Modifying the dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
print(student)
print(type(student))
# a) updating the elements (only values of dictionaries are updated)
student["age"] = 21
print(student)
# b) Adding the elements 
student["grade"] = "A" # directly add the key value pairs
print(student)
student.update({"Department":"Computer Enginnering","Year of graduation":2027})
print(student)
# c) Deleting the elements
student.pop("course")   # removes 'course'
print(student)
student.popitem()       # removes the last inserted key value pairs
print(student)
student.clear()         # removes all key value pairs
print(student)
del student             # removes the complete dictionaries from memeory
# print(student)        # if ran gives error like dict not defined

# 4. Some other methods in the dictionaries
# a) Sorting
my_dict = {"b": 5, "a": 2, "d": 8, "c": 1}
# sort by keys (ascending)
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)
# sort by keys (descending)
sorted_by_keys_desc = dict(sorted(my_dict.items(), reverse=True))
print(sorted_by_keys_desc)
# sort by values
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)
# sort by values(descending)
sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item:item[1], reverse=True))
print(sorted_by_values_desc)
# b) copy and refernces 
# c) copy vs reference (in dictionary)
a = {"name": "Alice", "age": 20}
# Reference (same memory)
b = a
b["age"] = 25
print("Reference change:", a)  # both changed — same dictionary
# To avoid this (make a copy)
b = a.copy()
b["age"] = 30
print("After copy:", a)        # separate dictionaries
