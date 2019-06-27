# n: the number of prisoners
# m: the number of sweets
# s: the chair number to begin passing out sweets from

# def saveThePrisoner(n, m, s):
#     if n == s:
#         return divmod(m, n)[1] + s - 1
#     return divmod((divmod(m, n)[1]+s-1), n)[1]

def saveThePrisoner(n, m, s):
    m = m % n
    if (s+m-1) % n <= n:
        if (s+m-1) % n == 0:
            return n
        return (s+m-1) % n

print(saveThePrisoner(4, 6, 2))  # 3
print(saveThePrisoner(5, 2, 1))  # 2
print(saveThePrisoner(5, 2, 2))  # 3
print(saveThePrisoner(7, 19, 2))  # 6
print(saveThePrisoner(3, 7, 3))  # 3
print(saveThePrisoner(3, 11, 3))  # 1
print(saveThePrisoner(6, 10, 5))  # 2
print(saveThePrisoner(11, 61, 5)) # 10
print(saveThePrisoner(53, 694907486, 2))  #197?
# 5 6 7 8 9 10 11 1 2 3 4 * 5 = 55
# 5 6 7 8 9 10
