#write a python program to convert temperature from Fahrenheit to celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Get user input for temperature in Fahrenheit
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius_output = fahrenheit_to_celsius(fahrenheit_input)

# Display the result
print(f"{fahrenheit_input} degrees Fahrenheit is equal to {celsius_output:.2f} degrees Celsius")
