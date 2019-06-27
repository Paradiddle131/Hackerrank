# i: starting day number
# j: ending day number
# k: divisor
def beautifulDays(i, j, k):
    reversedList = []
    count = 0
    countBeautiful = 0
    def isWhole(n):
        return n % 1 == 0
    def splitString(string):
        return [char for char in string]
    def reverse(splitted):
        reversedNo = ""
        for l in reversed(splitted):
            reversedNo += str(l)
        return int(reversedNo)
    for m in range(i, j+1):
        reversedList.append(reverse(splitString(str(m))))
        if isWhole(((m - reversedList[count]) / k)):
            countBeautiful += 1
        count += 1
    return countBeautiful


print(beautifulDays(20, 23, 6))  # 2