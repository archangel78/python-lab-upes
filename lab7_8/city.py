inputFile = open("lab7_8/city.txt","r")
cityData = inputFile.readlines()
cityNames = []
cityPop = []
cityArea = []

for city in cityData:
    current_city = city.split(" ")
    cityNames.append(current_city[0])
    cityPop.append(float(current_city[1]))
    cityArea.append(float(current_city[2]))

print("[*] City details: ")
for i in range(len(cityNames)):
    print("\n\tCity name: "+cityNames[i]+"\n\tCity populaltion: "+str(cityPop[i])+"\n\tCity Area: "+str(cityArea[i]))

print("[*] Cities with population more than 10L")
for i in range(len(cityNames)):
    if(cityPop[i]>10):    
        print("\n\tCity name: "+cityNames[i]+"\n\tCity populaltion: "+str(cityPop[i])+"\n\tCity Area: "+str(cityArea[i]))

totalArea = 0
for area in cityArea:
    totalArea+=area
print("\n[*] Total area of all cities: "+str(totalArea))