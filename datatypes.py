
# Data type is defined is as the type of datas that can be stored in variables.
# ex : int, strings, lists, dictionaries etc....

# 1. Numeric 
# a)int - integers(1,-2,0)
a = 10
print(a)
print(type(a))
# b)float - floating point numbers(3.14,-2.3,0.0)
b = 3.14
print(b)
print(type(b))
# c)complex - complex numbers(2+3j, 1-3j)
c = 2+3j
print(c)
print(type(c))

# 2. Sequence
# a)str - Strings("Melwin","This is code in python")
d = 'Melwin'
print(d)
print(type(d))
# b)list - List([1,2,3],["Mango","banana",1,2,3])
e = ["Mango","Watermelon","Apple",1,3.14,-9,2+3j]
print(e)
print(type(e))
# c)tuple - tuple((1,2,3,4),("Mango","Grapes",1,2,34,5))
f = ("Mango","Watermelon","Apple",1,3.14,-9,2+3j)
print(f)
print(type(f))

# 3. Mapping
# a)dict - Dictionaries( key - value pairs)
g = {
    "Name":"Melwin",
    "Roll_no":20,
    "Department":"Computer Engineering"
}
print(g)
print(type(g))

# 4. Set 
# a)set - Sets({1,2,3,4})
h = {"Mango","Watermelon","Apple",1,3.14,-9,2+3j}
print(h)
print(type(h))
# b)frozenset 
i = frozenset({1,2,3,4,5})
print(i)
print(type(i))

# 5. Boolean - (True or False)
x = True
print(x)
print(type(x))
y = False
print(y)
print(type(y))

