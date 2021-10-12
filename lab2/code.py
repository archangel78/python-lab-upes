#Code by Devakrishna Nair
n = int(input("Enter an integer: "))

#program 1
if (n%2)!=0:
    print("Weird")
else:
    if 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")
        
#program 2

for i in range(0,n):
    print(i*i)
    
#program 3

for i in range(1,n+1):
    print(i,end="")
