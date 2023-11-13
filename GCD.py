def GCD_fun(x,y):
    if (y==0):
        return x
    else:
        return GCD_fun(y,x%y) 
x=int(input("Enter first no:"))
y=int(input("Enter second no:"))
num=GCD_fun(x,y)
print("GCD of two number is:",num)         