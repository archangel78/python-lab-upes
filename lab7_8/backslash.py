inputFile = open("lab7_8/textfile","r")
outputFile = open("outfile","w")

fileData = inputFile.read()
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