#write a program to find the square root of number

import math

def calculate_square_root(number):
    if number < 0:
        return "Invalid input. Cannot calculate the square root of a negative number."
    else:
        square_root = math.sqrt(number)
        return square_root

# Get user input for the number
user_number = float(input("Enter a number: "))

# Calculate the square root
result = calculate_square_root(user_number)

# Display the result
print(f"The square root of {user_number} is {result:.2f}")
