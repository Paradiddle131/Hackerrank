def repeatedString(s, n):
    # divisor, remainder = divmod(n, len(s))[0], divmod(n, len(s))[1]
    # occIndexes = [key for (key, value) in enumerate(s) if value == 'a']
    # occAmount = len(occIndexes)
    # occAmountMult = occAmount*divisor

    # lastOccList = [key for (key, value) in enumerate(s) if value == 'a' and key < remainder]
    # lastOcc = len(lastOccList)

    # lastOcc = len(occIndexes[:remainder-1]) if remainder != 0 else 0

    # print("divisor      : ", divisor)
    # print("remainder    : ", remainder)
    # print("string       : ", s)
    # print("occIndexes   : ", occIndexes)
    # # print('lastOccList  : ', lastOccList)
    # print("lastOcc      : ", lastOcc)
    # print('occAmount    : ', occAmount)
    # print('occAmountMult: ', occAmountMult)
    # return occAmountMult + lastOcc
    # return s.count('a')*divisor + s[:remainder].count('a')
    return s.count('a')*divmod(n, len(s))[0] + s[:divmod(n, len(s))[1]].count('a')


print(repeatedString('abaa', 15))  # 9+2=11
print(repeatedString('abaa', 14))  # 9+1=10
print(repeatedString('abaa', 13))  # 9+1=10
print(repeatedString('abaa', 12))  # 9+0=9
print(repeatedString('abcac', 10))  # 4+0=4
print(repeatedString('a', 1000000000000))  # 1000000000000
