full_name = input("Enter full name: ")
initial_name = full_name[0]+"."
last_index = 0

for i in range(0,len(full_name)):
	if full_name[i]==" ":
		initial_name += full_name[i+1]+"."
		last_index = i

initial_name = initial_name[:len(initial_name)-2] + full_name[last_index:]

print("The initials are "+initial_name)