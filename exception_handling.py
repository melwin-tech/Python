# EXCEPTION HANDLING IN PYTHON

# 1 Basic try and except block
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")

# 2 Using else with try and except
try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("Number must be positive.")
except ValueError as e:
    print("Error:", e)
else:
    print("Great! You entered:", num)

# 3 Using finally block
try:
    file = open("example.txt", "r")
    print("File opened successfully.")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Finally block executed. File closed if it was opened.")
    try:
        file.close()
    except:
        pass

# 4 Catching multiple exceptions together
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Division result:", x / y)
except (ZeroDivisionError, ValueError) as e:
    print("An error occurred:", e)

# 6 Nested try-except
try:
    print("Outer try block starts.")
    try:
        n = int(input("Enter a number: "))
        print("10 divided by your number is:", 10 / n)
    except ZeroDivisionError:
        print("Inner Error: Division by zero.")
except Exception as e:
    print("Outer Error:", e)

# 7 Using assert statements for debugging
try:
    marks = int(input("Enter your marks (0-100): "))
    assert 0 <= marks <= 100, "Marks must be between 0 and 100."
    print("Your marks are:", marks)
except AssertionError as e:
    print("Assertion Error:", e)

# 10 Example combining all
try:
    print("Opening file...")
    file = open("example.txt", "r")
    data = file.read()
    print("File content:", data)
except FileNotFoundError:
    print("Error: example.txt not found.")
except PermissionError:
    print("Error: No permission to read file.")
except Exception as e:
    print("Unexpected Error:", e)
else:
    print("File read successfully.")
finally:
    print("Closing file if open.")
    try:
        file.close()
    except:
        pass
