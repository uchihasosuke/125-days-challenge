def calculate_LCM(x,y):
    if x>y:
        greater=x;
    else:
        greater=y;
    while(True):
        if((greater%x==0)and(greater%y==0)):
            LCM=greater;
            break;
        greater+=1
    return LCM 
num1=int(input("Enter First No:"))
num2=int(input("Enter second No:"))   
print("The LCM is",calculate_LCM(num1,num2))