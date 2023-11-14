#Create a Python class for a basic shape with constructor and methods to calculate area and perimeter

class Rectangle:

def_init_(self,length,breadth):

self.length-length self.breadth=breadth

def display(self): 
  print("Length of Reactangle is::",self.length)
  print("Breadth of Reactangle::",self.breadth)

def area(self): 
  return(self.length*self.breadth)

def perimeters(self): 
  return(2*self.length+2*self.breadth)

l=int(input("Enter the Length::")) 
b=int(input("Enter the Breadth::"))

r1=Rectangle(l,b) 
print("Reactangle object details are:")

r1.display()

print("")

print("Area of Reactanfle is= ",r1.area()) print("Perimeter of Rectangle is= ",r1.perimeters())
