#Create a python funciton to calculate the sum of natural numbers up to n


def sum_of_natural_numbers(n):
    if n < 0:
        return "Please enter a non-negative integer."
    else:
        sum_result = (n * (n + 1)) / 2
        return sum_result

# Get user input for the value of n
user_input = int(input("Enter a non-negative integer (n): "))

# Calculate the sum of natural numbers up to n
sum_result = sum_of_natural_numbers(user_input)

# Display the result
if isinstance(sum_result, str):
    print(sum_result)
else:
    print(f"The sum of natural numbers up to {user_input} is {sum_result}.")
