 
#Develop a Python program to demonstrate the concept of encapsulation using a class.
 
class Car:
 
    def __init__(self, make, model, year):
 
        self._make = make
 
        self._model = model
 
        self._year = year
 
 
    def get_make(self):
 
        return self._make
 
 
    def get_model(self):
 
        return self._model
 
 
    def get_year(self):
 
        return self._year
 
 
    def set_year(self, year):
 
        self._year = year
 
 
 
#Creating an instance of a car
 
my_car = Car("Tesla", "Model S", 2022)
 
 
#Accessing the attributes using getter methods
 
print("Car make:", my_car.get_make())
 
print("Car model:", my_car.get_model())
 
print("Car year:", my_car.get_year())
 
 
#Modifying the year attribute using a setter method
 
my_car.set_year(2023)
 
print("Modified car year:", my_car.get_year())

