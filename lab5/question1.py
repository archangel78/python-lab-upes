def add_numbers(n):
    sum = 0
    for i in range(1, n):
        sum+=i
    return str(sum)

def fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2,n):
        fib_series.append(fib_series[i-1]+fib_series[i-2])
    return fib_series

n = int(input("Enter a number: "))
print("The sum of first "+str(n)+" natural numbers is "+add_numbers(n))
print("The first "+str(n)+" terms of the fibonacci series are: "+str(fibonacci_series(n)[:n]))

