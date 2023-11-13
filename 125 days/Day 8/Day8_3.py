 
#Create a Python class for a basic calculator that can add, subtract, multiply, and divide.
 
class Calculator:
 
    def add(self, num1, num2):
 
        return num1 + num2
 
 
    def subtract(self, num1, num2):
 
        return num1 - num2
 
 
    def multiply(self, num1, num2):
 
        return num1 * num2
 
 
    def divide(self, num1, num2):
 
        if num2 != 0:
 
            return num1 / num2
 
        else:
 
            print("Error: Cannot divide by zero!")
 
 
# Creating an instance of the calculator
 
my_calculator = Calculator()
 
 
# Performing calculations
 
result_add = my_calculator.add(5, 3)
 
result_subtract = my_calculator.subtract(10, 4)
 
result_multiply = my_calculator.multiply(2, 6)
 
result_divide = my_calculator.divide(8, 2)
 
 
# Printing the results
 
print("Addition:", result_add)
 
print("Subtraction:", result_subtract)
 
print("Multiplication:", result_multiply)
 
print("Division:", result_divide)

