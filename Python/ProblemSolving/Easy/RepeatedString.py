def repeatedString(s, n):
    divisor, remainder = divmod(n, len(s))[0], divmod(n, len(s))[1]
    occIndexes = [key for (key, value) in enumerate(s) if value == 'a']
    occAmount = len(occIndexes)
    occAmountMult = occAmount*divisor

    lastOccList = [key for (key, value) in enumerate(s) if value == 'a' and key < remainder]
    lastOcc = len(lastOccList)
    print("string       : ", s)
    print("occIndexes   : ", occIndexes)
    print('lastOccList  : ', lastOccList)
    print('occAmount    : ', occAmount)
    print('occAmountMult: ', occAmountMult)
    return occAmountMult + lastOcc



print(repeatedString('abaa', 15))  # 9+2=11
print(repeatedString('abcac', 10))  # 4+0=2
print(repeatedString('a', 1000000000000))  # 1000000000000
