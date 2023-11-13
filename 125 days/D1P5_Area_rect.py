def Rectangle(length,width):
    area=length*width
    return area

length=float(input("Enter length of rectangle: "))
width=float(input("Enter width of rectangle: "))
area=Rectangle(length,width)
print(f"Area of rectangle is: {area}")
