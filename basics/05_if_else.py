"""
Topic: Conditional Statements (if, elif, else)
Author: Pankaj Sharma
Description: Demonstrates basic conditional logic using if, elif, and else statements.

"""

# Example 1: Basic if statement
print(f"Example 1: Basic if statement")

age = 18
print(f"Age: {age}")
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("\n-----------------------------\n")

# Example 2: Using elif for multiple conditions
print(f"Example 2: Using elif for multiple conditions")

score = 85
print(f"Score: {score}")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


print("\n-----------------------------\n")
# Example 3: Nested if statements
print(f"Example 3: Nested if statements")
number = 15
print(f"Number: {number}")
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")