input = input("Enter string to count alphabets: ")
alphabet_counter = {}

for i in input.upper():
	alphabet_counter[i] = alphabet_counter.get(i,0)+1

print("The occurences of alphabets are: ")
for alphabet in alphabet_counter:
	print(alphabet+": "+str(alphabet_counter[alphabet]))
