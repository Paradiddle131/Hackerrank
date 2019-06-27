import math
import os
import random
import re
import sys

def breakingRecords(scores):
    lowestScore = sys.maxsize
    highestScore = -1
    countMin = -1
    countMax = -1
    for i in scores:
        if i > highestScore:
            highestScore = i
            countMax += 1
        if i < lowestScore:
            lowestScore = i
            countMin += 1
    return [countMax, countMin]


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))