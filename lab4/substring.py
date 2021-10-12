original_string = input("Enter a string: ")
substring = input("Enter a sub-string to check number of occurences: ")

count = 0
for i in range(0, len(original_string)):
	if original_string[i:len(substring)+i]==substring:
		count=count+1

print("The substring occurs "+str(count)+" times")