def findDigits(n):
    countDivisor = 0
    def splitString(string):
        return [char for char in string]
    splitted = splitString(str(n))
    for i in range(len(splitted)):
        number = int(splitted[i])
        if number == 0:
            continue
        elif n % number == 0:
            countDivisor += 1
    return countDivisor

print(findDigits(12))  # 2
print(findDigits(1012))  # 3