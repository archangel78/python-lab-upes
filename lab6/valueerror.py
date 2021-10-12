import math

num = int(input("Enter number to find square root of: "))
try:
    sqrt = math.sqrt(num)
    print("the square root of "+str(num)+" is "+str(sqrt))
except ValueError:
    print("Invalid Value entered")
