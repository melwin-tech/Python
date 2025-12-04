
# Operators are symbol which are used to perform some operation on the operands
# ex : +,-,*,/,<,>,== etc...

# 1. Arithmetic operators
# its is a binary operators which are used to perform arithmetic calculations
a = 5
b = 3.2
print("a = ",a)
print("b = ",b)
print("Addition of a and b is : ", a+b)
print("Subtraction of a and b is : ", a-b)
print("Multiplication of a and b is : ", a*b)
print("Division of a and b is : ", a/b)
print("Floor division of a and b is : ", a//b)
print("Modulo of a and b is : ", a%b)
print("Power of a to b is : ", a**b)

# 2. Relational operators
# its a binary operator which is used to compare two operands
x = 5
y = 3
print("x = ",x)
print("y = ",y)
print("a Greater than b : ", x > y)
print("a Greater than equal to b : ", x >= y)
print("a Smaller than b : ", x < y)
print("a Smaller than equal to b : ", x <= y)
print("a Equal to b : ", x == y)
print("a Not Equal to b : ", x != y)

# 3. Assignment operators
# its a unary operator which is used to do the arithmetic operations with itself
x = 3
print("x = ",x)
print("x++ : ", x+1)
print("x-- : ", x-1)
print("x*2 : ", x*2)
print("x/4 : ", x/4)
print("x%5 : ", x%5)

# 4. Logical operators 
# its a binary operator which is used to perform logical and,not,or operations with operands
a = True
b = False
print("a = ",a)
print("b = ",b)
print("a and b gives : ",a and b)
print("a or b gives : ",a or b)
print("a not b gives : ",not a)

# 5. Bitwise operators
# its a binary operators which is used to perform bit by bit operations
a = 10
b = 4
print("a = ",a)
print("b = ",b)
print("a bitwise and with b gives : ",a & b)
print("a bitwise or with b gives : ",a | b)
print("a bitwise not with b gives : ",~a)
print("a bitwise xor with b gives : ",a ^ b)
print("a bitwise right shift with b gives : ",a >> 2)
print("a bitwise left shift with b gives : ",a << 2)

# 6. membership operator
# in and not in are the membership operators that are used to test whether a value or variable is in a sequence.
x = 24
y = 20
list_1 = [10, 20, 30, 40, 50]
print("x = ",x)
print("y = ",y)
print("list_1 = ",list_1)
print("x in list_1 : ", x in list_1)
print("x not in list_1 : ", x not in list_1)
print("y in list_1 : ", y in list_1)
print("y not in list_1 : ", y not in list_1)

# 7. Identity operators
# is and is not are the identity operators both are used to check if two values are located on the same part of the memory.
a = 10
b = 20
c = a
print("a = ",a)
print("b = ",b)
print("a = ", c)
print("a is not in b gives : ",a is not b)
print("a is in c gives : ",a is c)