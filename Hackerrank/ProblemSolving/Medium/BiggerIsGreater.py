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
    for i in reversed(range(len(asc))):
        try:
            if asc[-1] > asc[i - 1]:
                asc[-1], asc[i - 1] = asc[i - 1], asc[-1]
                break
            else:
                continue
        except:
            pass
    return toChar(asc)


print(biggerIsGreater("hefg"))  # hegf [104,101,102,103] - [104,101,103,102]
print(biggerIsGreater("dhck"))  # dhkc
print(biggerIsGreater("dkhc"))  # hcdk
print(biggerIsGreater("adbf"))  # badf
