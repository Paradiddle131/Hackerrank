def biggerIsGreater(w):
    def splitString(word):
        return [char for char in word]
    def ASCII(chars):
        listASCII = []
        for i in range(len(chars)):
            listASCII.append(ord(chars[i]))
        return listASCII
    def reverseList(list):
        rev = []
        for i in reversed(range(len(list))):
            rev.append(list[i])
        return rev
    asc = ASCII(splitString(w))
    reversedList = reverseList(asc)
    for i in reversed(range(len(asc))):
            try:
                if asc[i] > asc[i-1]:
                    asc[i], asc[i-1] = asc[i-1], asc[i]
                    break
            except:
                continue
    return asc


print(biggerIsGreater("hefg"))  # hegf