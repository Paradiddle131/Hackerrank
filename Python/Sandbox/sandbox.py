"""

s= [1, 2, 32, 16, 4, 6]
i = 4
m = 2
#print(sum(s[i:i+m]))
#print(s[i:i+m])



#if len(list) == m:
 #   count += 1

list = [1,2,3,4]
for m in list[1:]:
    print(m)
    print(list.index(m))
    print(list.index(3))

ar = [1, 3, 2, 6, 1, 2]
if(ar[0] + ar[2]) % 3 == 0:
    print(True)
    print(ar[0] + ar[2])
if ar[0] < ar[2]:
    print(True)
if ar[0] < ar[2] and (ar[0] + ar[2]) % 3 == 0:
    print(True)
else:
    print(False)
"""
import math

string = "43 95 51 55 40 86 65 81 51 20 47 50 65 53 23 78 75 75 47 73 25 27 14 8 26 58 95 28 3 23 48 69 26 3 73 52 34 7 40 33 56 98 71 29 70 71 28 12 18 49 19 25 2 18 15 41 51 42 46 19 98 56 54 98 72 25 16 49 34 99 48 93 64 44 50 91 44 17 63 27 3 65 75 19 68 30 43 37 72 54 82 92 37 52 72 62 3 88 82 71"
string2 = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5"

string3 = "104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149"

string4 = "422346306 940894801 696810740 862741861 85835055 313720373"

#print(spl)
"""
for s in range(0, len(string2)):
    print(spl[s] + ",", end=" ")
    spl2 = spl[s] + ","



bill = [3, 10, 2, 9]
print(bill.remove(bill[1]))
billB = bill.remove(bill[1])
#charge = sum(billB)/2
print(billB)
"""
"""
print(ord('a'))
print(chr(97))

drives = [1, 2, 3]
print(drives[-1])
"""
"""
for x in range(104,104+45+1):
    print(x, end =" ")
"""
spl = string4.split(" ")
"""
for x in range(0,104):
    print(x, end =" ")
"""
"""
for s in range(0, len(string4)):
    print(spl[s] + ",", end=" ")
    spl2 = spl[s] + ","
    """
#print(range(104, len(spl)))

def splitString(word):
    return [char for char in word]
"""
word = 'geeks'
print(splitString(word))
print(splitString(word)[3])
print(len(splitString(word)))

isBelowSurface = False
currentLevel = 0
mountain = 0
if isBelowSurface is False and currentLevel == 0:
    mountain += 1
print("mountain: ", mountain)

S = [1, 7, 2, 4]
print(S[1:])

print(divmod(11, 3))
print(divmod(11, 3)[1])
print(divmod(11, 3)[1] is not 0)

print(divmod(4, 3))
print(divmod(4, 3)[1])
print(divmod(4, 3)[1] is not 0)"""

# word = "haveaniceday"
# word = "feedthedog"
# letters = splitString(word)
# length = len(letters)
# lowerRoot = math.floor(math.sqrt(12))
# upperRoot = math.ceil(math.sqrt(12))
# rows = lowerRoot
# cols = upperRoot
# picked = ""
# parts = []
# combined = []
# stringAgain = ""
# vertical = []
# count = 0
# def combineString(s):
#     new = ""
#     for x in s:
#         new += x
#     return new
# for i in range(0, len(letters)+1, 4):
#     if i < len(letters):
#         parts.append(letters[i:i+4])
#         if len(combined) < 3:
#             combined.append(combineString(parts[count]))
#     count += 1
#
# print("parts: ", parts)
"""
letters2 = splitString(combined)
stringAgain = stringAgain.join(letters2)
#for j in range(0, len(combined)+1):
#    vertical.append(combined[j])
for k in range(rows+1): # 0 1 2 3
    for l in range(0, len(letters), cols): # 0 4 8
        picked = picked.__add__(letters[k+l])
        if l == (rows-1)*cols:
            picked = picked.__add__(" ")
#splittedResult = picked.split()
print("length: ", length)
print("lowerRoot: ", lowerRoot)
print("upperRoot: ", upperRoot)
print("picked: ", picked)

print("letters: ", letters)
print("second letter: ", letters[1])
print("parts: ", parts)
print("part: ", parts[0][1])
print("combined parts", combined)
print("string Again", stringAgain)
print("letters2", letters2)
#print(combineString(parts[0]))
#parts[i][:len(parts)]
partsList = []
print(len(parts))
print(parts[0])
print(len(parts[0]))
#for i in range(len(parts)):
#    for j in range(len(parts[i])):
for x, y, z in zip(*parts):
    print(x, y, z)
        #partsList = partsList.append(parts[i])
print(partsList)
"""
"""
trys = ['have', 'anic', 'eday']
mystr = ""
joined = mystr.join(trys)
print(joined)
"""

print(divmod(19, 7))