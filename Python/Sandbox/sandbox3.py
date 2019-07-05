# def splitString(string):
#     return [char for char in string]
# number = 230
# print(splitString(str(number)))

# mylist = [1,2,3]
# for i in reversed(mylist):
#     print(i)

# s = "abcdefgh"
# print(s[0])
# print(s[0:3])

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5. print Not Wei rd
#If n is even and in the inclusive range of 6 to 20. print Wei rd
#If n is even and greater than 20. print Not Weeird

# n = 3
#
# if n % 2 != 0:
#     print("Weird")
# if (n % 2 == 0) & ((n <= 6) or (n >= 2)):

# print("a" < "ba")
# print(ord("a"))

"""
numbers = [100, 107, 104, 99]
numbers2 = numbers
numbers2[0] = max(numbers)
print(numbers)
print(numbers2)
def biggerIsGreater(w):
    def splitString(word):
        return [char for char in word]

    def toASCII(chars):
        listASCII = []
        for i in range(len(chars)):
            listASCII.append(ord(chars[i]))
        return listASCII

    def toChar(ASCII):
        string = ""
        for i in range(len(ASCII)):
            string += ((chr(ASCII[i])))
        return string
    asc = toASCII(splitString(w))
    def makeGreatAgain(list):
        listRes = []
        if list[0] != max(list):
            list[0] = min(list[1:])
        listRes = listRes.append(list[0])
        listRes = listRes.append(sorted(list[1:]))
        return listRes
    res = makeGreatAgain(asc)
    return res


print(biggerIsGreater("hefg"))  # hegf [104,101,102,103] - [104,101,103,102]
print(biggerIsGreater("dhck"))  # dhkc
print(biggerIsGreater("dkhc"))  # hcdk
print(biggerIsGreater("adbf"))  # badf

"""
from typing import OrderedDict

myinput = "68 81 46 54 30 11 19 23 22 12 38 91 48 75 26 86 29 83 62"
rep = myinput.replace(" ", ", ")
print(rep)

# spl = myinput.split(" ")
# def commaAdder(s):
#     for i in s:
#         print(i, ",")


# print(commaAdder(spl))

# def flatlandSpaceStations(n, c):
#     localMin = 0
#     for city in range(n):
#         for statcity in c:
#             if statcity == c[0]:
#                 localMin = abs(city - min(c))
#             if localMin < abs(city - statcity):
#                 localMin = abs(city - statcity)
#
#     return localMin

# def flatlandSpaceStations(n, c):
#     maxdiff = 0
#     for i in range(n):
#         diff = 0
#         for j in c:
#             if j == c[0]:
#                 diff = abs(i-j)
#             elif diff > abs(i-j):
#                 diff = abs(i-j)
#         if maxdiff < diff:
#             maxdiff = diff
#     return maxdiff

# def repeatedString(s, n):
#     def splitString(word):
#         return [char for char in word]
#     count = 0
#     divisor, remainder = divmod(n, len(s))[0], divmod(n, len(s))[1]
#     # for char in splitString(s):
#     #     if char == 'a':
#     #         count += 1
#     for i in range(len(splitString(s))*divisor):
#         if splitString(s)[i % len(s)] == 'a':
#             count += 1
#     return count
#
#
# print(repeatedString('aba', 8))

# def repeatedString(s, n):
#     count = 0
#     divisor, remainder = divmod(n, len(s))[0], divmod(n, len(s))[1]
#     occIndexes = [key for (key, value) in enumerate(s) if value == 'a']
#     occAmount = len(occIndexes)
#     occAmountMult = occAmount*divisor
# 
#     lastOccList = [key for (key, value) in enumerate(s) if value == 'a' and key < remainder]
#     lastOcc = len(lastOccList)
#     # occLast = occIndexes[:s.index(remainder)]
#     print("string       : ", s)
#     print("occIndexes   : ", occIndexes)
#     print('lastOccList  : ', lastOccList)
#     # print('occAll       : ', occAll)
#     print('occAmount    : ', occAmount)
#     print('occAmountMult: ', occAmountMult)
#     # print('occLast', occLast)
#     return occAmountMult + lastOcc
# 
# 
# print(repeatedString('abaa', 15))  # 9+2=11
# 

# mydict = {x: x * x for x in range(10)}
# print(mydict)

def minimumDistances(a):
    dictNums = {}
    dupCount = 0
    for number in range(10):
        for (key, value) in enumerate(a):
            if value == number:
                dupCount += 1
                dictNums['{}'.format(number)] = dupCount
            # dictNums.update(dupCount)
        dupCount = 0
    return dictNums


# print(minimumDistances([7, 1, 3, 4, 1, 7]))  # 3 (4-1)

# dictIndexes = {}
#     for number in range(10):
#         for (key, value) in enumerate(a):
#             if value == number:
#                 dictIndexes['{}'.format(value)] = key
#                 dictIndexes.update({'{}'.format(value): dictIndexes[key] + key})

print(minimumDistances([7, 1, 3, 4, 1, 7]))  # 3 (4-1)

dictSample = {'1': 2, '3': 1, '4': 1, '7': 2}
dictSampleOrdered = OrderedDict("a", "1"), ("c", '3'), ("b", "2")
print(list(dictSample.values())[3])
dictSampleOrdered.index('c')