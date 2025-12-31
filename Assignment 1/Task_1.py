"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division

"""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

Addition = a + b
Subtraction = a - b
Multiplication = a * b
Division = a / b if b != 0 else "Undefined (cannot divide by zero)"

print(f"Addition: ", Addition)
print(f"Subtraction: ", Subtraction)
print(f"Multiplication: ", Multiplication)
print(f"Division:", Division) 