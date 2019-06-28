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