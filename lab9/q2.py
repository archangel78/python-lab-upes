mylist = [1,2,3,"4",5, "#"]
sum = 0

for i in mylist:
    try:
        sum = sum + i
    except TypeError:
        try:
            sum = sum + int(i)
        except ValueError:
            print("Value error occured, could not add: "+i)

print(sum)
print(mylist)