from os import uname
from random import randint

myList = []
uniqueList = []

for i in range(100):
    generatedRandom = randint(0, 9)
    myList.append(generatedRandom)
    if generatedRandom not in uniqueList:
        uniqueList.append(generatedRandom)

print("list is:")
print(myList)
print("unique list is:")
print(uniqueList)
print("Unique sorted list is: ")
# sortedList = [int(x) for x in uniqueList]
# sortedList = sorted(sortedList, key = int)
sortedList = sorted(uniqueList)
print(sortedList)
