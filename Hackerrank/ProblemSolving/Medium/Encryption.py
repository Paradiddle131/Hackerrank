import math

def encryption(s):
    def splitString(s):
        return [char for char in s]
    letters = splitString(s)
    rows = math.floor(math.sqrt(len(letters)))
    cols = math.ceil(math.sqrt(len(letters)))
    picked = ""
    for row in range(rows + 1):  # 0 1 2 3
        for col in range(0, len(letters), cols):  # 0 4 8
            picked = picked.__add__(letters[row + col])
            if col == (rows - 1) * cols:
                picked = picked.__add__(" ")
    return picked


#print(encryption("haveaniceday")) #hae and via ecy (have anic eday)
print(encryption("feedthedog")) #fto ehg ee dd (feed thed og)