import os
import sys

def getTotalX(a, b):
    #countFactor = 0
    #countElement = 0
    countF = 0
    countE = 0
    listF = []
    listE = []
    for i in range(min(a),min(b)+1):
        for j in range(0,len(a)):
            if i % a[j] == 0:
                countF += 1
        if countF == len(a):
            listF.append(i)
        countF = 0
    for k in range(len(listF)):
        for l in b:
            if l % listF[k] == 0:
                    countE += 1
        if countE == len(b):
            if listF[k] not in listE:
                listE.append(listF[k])
        countE = 0
    return listE


print(getTotalX([2, 4], [16, 32, 96]))

"""
for k in range(min(b),max(b)+1):
    for l in range(0,len(b)):
        if k % b[l]:
            countE += 1
    if countE == len(b):
        listE.append(k)
    countE = 0

intersection = list(set(listE).intersection(listF))
print(listF)
print(listE)
return intersection

"""