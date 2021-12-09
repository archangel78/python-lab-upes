try:
    inputFile = open("lab9/TestFile1.txt","w")
    fileData = inputFile.read()
except FileNotFoundError:
    print("[*] Input file does not exist")
    exit()
except EOFError:
    print("[*] No content in file")
    exit()

outputFile = open("TestFile2.txt","w")
outputData = ""

for char in fileData:
    if(char=="\""):
        outputData+="\\\""
    else:
        outputData+=char

print("[*] Writing output into \"outputFile\"")
outputFile.write(outputData)
print("\n[*] Original contents of file: \n"+fileData+"\n\n[*] Edited contents of file: \n"+outputData)
inputFile.close()
outputFile.close()