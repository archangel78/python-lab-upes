a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

try:
    c = a/b
    print("Quotient is: "+str(c))
except ZeroDivisionError:
    print("Can't divide by zero")