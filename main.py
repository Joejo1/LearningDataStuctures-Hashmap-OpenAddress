import numpy as np
import pandas as pd
import csv

emtyKey = '........'
ar = np.array([[emtyKey]* 2] * 20000)
ln = len(ar)
numOfCollision = 0

#------------------methods

def getHash(key, arLen):
    index = hash(key) % arLen
    return index

def setArKey(index, key):
    ar[index][0] = key

def isKeyMatching(index, key):
    if ar[index][0] == key:
        return True
    else:
        return False

def isCollision(index, key):
    if ar[index][0] == emtyKey:
        return False
    else:
        return True

#--------------------MAIN

js = np.array(pd.read_csv("name.csv"))

lengthOfCSV = len(js)
print(lengthOfCSV)
j = 0

for i in js:
    key = js[j][0]
    #value = js[j][3]

    index = getHash(key, ln)

    collision = False
    collision = isCollision(index, key)
    collisionOffset = 0
    while collision == True:
        collisionOffset = collisionOffset+1
        collision = isCollision(index-collisionOffset, key)
        numOfCollision = numOfCollision + 1

    ar[index-collisionOffset][0] = key
    #ar[index-collisionOffset][1] = value
    collisionOffset = 0

    j = j + 1



#----------Check how many are populated
emty = 0
full = 0
l = 0
for k in ar:
    if ar[l][0] == emtyKey:
        emty = emty + 1
    else:
        full = full + 1

    l = l + 1


with open("output.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(ar)



#-----------------Printing-----------
print('Populated:', full, 'Empty:', emty)

print('number of collisions: ', numOfCollision)

#print(js)

#print(ar)

