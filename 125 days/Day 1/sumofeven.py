#Write a program to find the sum of even numbers in a list
def sumofeven(list):
    esum=0
    for num in list:
        if(num%2==0):
            esum=esum+num
    return esum

num=[8,10,18,5,4,24,7]
result=sumofeven(num)
print(f"sum of even numbers in the list is: {result}")
