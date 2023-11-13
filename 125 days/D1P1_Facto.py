def fact(n):
    if(n==0) or (n==1):
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter a number: "))
factorial=fact(num)
print(f"The factorial of {num} is: {factorial}")
