#implement a program to calculate the area of circle
import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

# Get user input for the radius of the circle
radius_input = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
circle_area = calculate_circle_area(radius_input)

# Display the result
print(f"The area of the circle with radius {radius_input} is {circle_area:.2f}")
