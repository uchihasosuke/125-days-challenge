#develop a python program to calculate the simple interest


def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Get user input for principal amount, interest rate, and time
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
time_in_years = float(input("Enter the time in years: "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal_amount, interest_rate, time_in_years)

# Display the result
print(f"The simple interest for a principal amount of ${principal_amount}, an interest rate of {interest_rate}%, and a time period of {time_in_years} years is ${simple_interest:.2f}")


