
# Sets is sequenece data type which is unordered, muteable, not allow duplicate values of the collections of the items
# ex : my_set = {1,2,3,4} etc ...

# 1. Creation of the sets
# a) by directly
myset = {10, 20, 30, 40}
print(myset)
print(type(myset))
# b) by set constructor
myset = set([10, 20, 30, 40])
print(myset)
print(type(myset))

# 2. Acessing the elements of the sets
# You cannot access the elements as you access in the list because its unordered.
# so the approach is loops
for i in myset:
    print(i)

# 3. Modification in the sets
# a) Updating the elements
# here you cannot the update the elements as it not having the proper index .
# b) Adding the elements
fruits = {"apple", "banana"}
fruits.add("cherry") # adds one items to set
print(fruits)
fruits.update(["mango", "grapes", "banana"])  # add mulitple items using update()
print(fruits)
# c) Deleting the items from the sets
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") # give error if the items given not found
print(fruits)
fruits.discard("banana") # give no error if the items given not found
print(fruits)
fruits.pop() # pops the random items
print(fruits)
fruits.clear() # remove all items from the set
print(fruits)

# 4. Some important methods in the sets
# a) Set Operations Example 
# Define two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Set A:", A)
print("Set B:", B)
# Union
print("Union:", A.union(B))
# Intersection
print("Intersection:", A.intersection(B))
# Difference
print("Difference (A - B):", A.difference(B))
# Symmetric Difference
print("Symmetric Difference:", A.symmetric_difference(B))
# issubset
print("Is A subset of B?:", A.issubset(B))
# issuperset
print("Is A superset of B?:", A.issuperset(B))
# isdisjoint
print("Are A and B disjoint?:", A.isdisjoint(B))
# b) copy and refernces
a = {1, 2, 3}
b = a
b.add(4)
print(a)  # {1, 2, 3, 4} — both changed
a = {1, 2, 3}
b = a.copy()
b.add(4)
print(a)  # {1, 2, 3} - not changed
print(b)  # {1, 2, 3, 4}

