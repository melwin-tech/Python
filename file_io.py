import os

# 1 Create and Write to a File
with open("example.txt", "w") as file:
    file.write("Line 1: Hello, Python File Handling!\n")
    file.write("Line 2: This is the second line.\n")
    file.write("Line 3: Learning file operations in Python.\n")

print("File 'example.txt' created and initial content written.")

# 2 Read Entire File
with open("example.txt", "r") as file:
    content = file.read()
    print("Reading entire file:")
    print(content)

# 3 Read Line by Line Using readline()
with open("example.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print("Reading two lines using readline():")
    print("Line 1:", line1.strip())
    print("Line 2:", line2.strip())

# 4 Read All Lines into a List Using readlines()
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Reading all lines using readlines():")
    print(lines)

# 5 Append Data to the Same File
with open("example.txt", "a") as file:
    file.write("Line 4: This line is appended.\n")
    file.write("Line 5: Appending more data to the file.\n")

print("Data appended successfully.")

# 6 Check File Existence
if os.path.exists("example.txt"):
    print("File 'example.txt' exists.")
else:
    print("File not found.")

# 7 Read File Line by Line Using Loop
with open("example.txt", "r") as file:
    print("Reading file line by line using loop:")
    for line in file:
        print(line.strip())

# 8 Copying File Content to Another File
with open("example.txt", "r") as src:
    data = src.read()

with open("example_copy.txt", "w") as dest:
    dest.write(data)

print("File copied successfully to 'example_copy.txt'.")

# 9 Demonstrate tell() and seek() Methods
with open("example.txt", "r") as file:
    print("Demonstrating tell() and seek():")
    data = file.read(10)
    print("First 10 characters:", data)
    print("Current pointer position:", file.tell())
    file.seek(0)
    print("Reading again from start:")
    print(file.read(10))

# 10 Error Handling (Safe Read)
try:
    with open("non_existing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found, please check the filename.")
except PermissionError:
    print("Error: No permission to read this file.")

# 11 Delete File (optional demonstration)
# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("File 'example.txt' deleted successfully.")
# else:
#     print("File 'example.txt' not found for deletion.")

# 12 File Mode Reference (in comments)
"""
r  -> Read mode (default)
w  -> Write mode (creates or overwrites file)
a  -> Append mode (adds data at end)
x  -> Create mode (error if file exists)
r+ -> Read and Write
t  -> Text mode (default)
b  -> Binary mode
"""
