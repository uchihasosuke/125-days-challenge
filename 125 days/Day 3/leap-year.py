#Write a python program to check if a year is a leap year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get user input for the year
user_year = int(input("Enter a year: "))

# Check if the year is a leap year
result = is_leap_year(user_year)

# Display the result
if result:
    print(f"{user_year} is a leap year.")
else:
    print(f"{user_year} is not a leap year.")
