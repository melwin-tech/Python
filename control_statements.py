
# # Control statements are special statements in Python that control the flow of execution of the program — that is, they decide which part of the code runs and when.
# # ex : if there is rain today then we will not play cricket

# # 1. if statements
# The if statement executes a block of code only if a condition is True.
age = 18
if age >= 18:
    print("You are an adult.")

# 2. if-else statements
# The else part runs if the condition in the if statement is False.
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3. if-elif-else statements
# Used when you have multiple conditions to check.
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# 4) match-case statements
# match-case works like a switch statement in other languages.
# It checks a variable against several patterns.
day = "Monday"
match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Weekend is near")
    case "Sunday":
        print("Relax, it's Sunday")
    case _:
        print("Midweek day")

# 5) nested if-else
# You can place one if-else statement inside another.
# Used for multiple-level conditions.
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")

# you can use nested with if , if-else, if-elif-else and many more
