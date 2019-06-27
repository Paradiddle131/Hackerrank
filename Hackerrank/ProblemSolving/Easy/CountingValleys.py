def countingValleys(n, s):
    isBelowSurface, posOne, negOne = (False,)*3
    currentLevel, double, mountain, valley = (0,)*4
    if (s[0] == "U"):
        posOne = True
    else:
        negOne = True
    def splitString(s):
        return [char for char in s]
    for i in range(len(splitString(s))):
        if double % 2 == 0:
            double = 0
        if i != 0:
            posOne = True if currentLevel == 1 else False
            negOne = True if currentLevel == -1 else False
        if(s[i] == "U"):
            currentLevel += 1
            double += 1
        if(s[i] == "D"):
            currentLevel -= 1
            double += 1
        if isBelowSurface is False and currentLevel == 0: mountain += 1
        if isBelowSurface is True and currentLevel == 0: valley += 1
        isBelowSurface = True if currentLevel < 0 else False
        #if(posOne is True & isBelowSurface is False): mountain += 1
        #if(negOne is True & isBelowSurface is True): valley += 1

    return valley

print(countingValleys(8, "UDDDUDUU"))  # 1
print(countingValleys(10, "UDDDUDUUDU"))  # 2
print(countingValleys(14, "UDDDUDUUDUUUDD"))  # 2