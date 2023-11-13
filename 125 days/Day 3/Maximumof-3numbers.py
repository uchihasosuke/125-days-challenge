#implement a program to find the maximum of three numbers

def find_maximum(num1, num2, num3):
    max_number = max(num1, num2, num3)
    return max_number

# Get user input for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum of the three numbers
maximum_number = find_maximum(num1, num2, num3)

# Display the result
print(f"The maximum of {num1}, {num2}, and {num3} is {maximum_number}.")
