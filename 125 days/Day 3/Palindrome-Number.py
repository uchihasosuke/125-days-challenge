#Develop a python program to check if a number is palindrome

def is_palindrome(number):
    # Convert the number to a string for easier comparison
    num_str = str(number)
    
    # Check if the reversed string is equal to the original string
    return num_str == num_str[::-1]

# Get user input for the number
user_number = int(input("Enter a number: "))

# Check if the number is a palindrome
result = is_palindrome(user_number)

# Display the result
if result:
    print(f"{user_number} is a palindrome.")
else:
    print(f"{user_number} is not a palindrome.")
