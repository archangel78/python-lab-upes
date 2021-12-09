inputFile = open("lab7_8/rythm.txt","r")
outputFile = open("lab7_8/words.txt","w")
fileData = inputFile.read()
unique_words = {}
words = fileData.replace("\n"," ").split(" ")

for word in words:
    unique_words[word.lower()] = "x"

print("[*] Writing unique words to \"words.txt\"")
print("[*] The unique words given in the file are: ")
for word in unique_words:
    print(word+", ",end="")
    outputFile.write(word+"\n")
print()
inputFile.close()
outputFile.close()