import math

# def encryption(s):
#     def splitString(s):
#         return [char for char in s]
#     letters = splitString(s)
#     rows = math.floor(math.sqrt(len(letters)))
#     cols = math.ceil(math.sqrt(len(letters)))
#     picked = ""
#     for row in range(rows + 1):  # 0 1 2 3
#         for col in range(0, len(letters), cols):  # 0 4 8
#             picked = picked.__add__(letters[row + col])
#             if col == (rows - 1) * cols:
#                 picked = picked.__add__(" ")
#     return picked
#
#
# #print(encryption("haveaniceday")) #hae and via ecy (have anic eday)
# print(encryption("feedthedog")) #fto ehg ee dd (feed thed og)

def encryption(s):
    parts = []
    if math.floor(math.sqrt(len(s))) * math.ceil(math.sqrt(len(s))) < len(s):
        rows = cols = math.ceil(math.sqrt(len(s)))
    else:
        rows = math.floor(math.sqrt(len(s)))
        cols = math.ceil(math.sqrt(len(s)))
    def splitString(s):
        return [char for char in s]
    letters = splitString(s)
    def seperate(whole):
        for i in range(0, len(letters) + 1, cols):
            if i < len(letters):
                parts.append(letters[i:i + cols])
        return parts
    parts = seperate(letters)
    string3 = ""
    count = 0
    missing = len(parts[0]) - len(parts[-1])
    for i in range(cols):
        printedCount = 0
        countPass = 0
        for x in parts:
            if countPass == 1:
                pass
            else:
                try:
                    string3 += x[i]
                except:
                    pass
                printedCount += 1
                count += 1
                if ((len(parts[0]) - missing) == i) & (x == parts[rows-2]) & (count > 1*printedCount):
                    string3 += " "
                    countPass += 1
                    pass
                else:
                    if x == parts[rows-1]:
                        string3 += " "
    return string3

# print(encryption("haveaniceday")) #hae and via ecy (have anic eday)
# print(encryption("feedthedog")) #fto ehg ee dd (feed thed og)


s=input()
sm=s.replace(" ","")
r=math.floor(math.sqrt(len(sm)))
c=math.ceil(math.sqrt(len(sm)))
for i in range(c):
    print(sm[i::c],end=" ")
# https://www.hackerrank.com/challenges/encryption/forum/comments/160696
