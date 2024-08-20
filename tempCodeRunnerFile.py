# Program to find the sum of natural using recursive function

def recur(x):
    if (x<=1):
        return x
    else:
        return x+recur(x-1)
#change value for different result
num=4
if(num<0):
    print("Enter a positive number")
else:
    print("The sum is",recur(num))