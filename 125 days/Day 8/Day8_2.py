 
#Write a Python program to create an instance of a car object with attributes like make, model, and year
 
class Car:
 
    def __init__(self, make, model, year):
 
        self.make = make
 
        self.model = model
 
        self.year = year
 
 
# Creating an instance of a car
 
my_car = Car("Tesla", "Model S", 2021)
 
 
# Printing the attributes of the car
 
print("Car make:", my_car.make)
 
print("Car model:", my_car.model)
 
print("Car year:", my_car.year)
 
