stamp_set = set([])
no_stamps = int(input("Enter total number of stamps: "))

for i in range(0,no_stamps):
    stamp = input("Enter country "+str(i+1)+" name: ")
    stamp_set.add(stamp)

print("\nThere are "+str(len(stamp_set))+" unique stamps: ")
print(stamp_set)