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

print("Addition: ", Addition)
print("Subtraction: ", Subtraction)
print("Multiplication: ", Multiplication)
print("Division:", Division) 

"""
Output:
Enter the first number: 5
Enter the second number: 2.5
Addition: 7.5
Subtraction: 2.5
Multiplication: 12.5
Division: 2.0
"""