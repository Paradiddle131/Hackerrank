def extraLongFactorials(n):
    # return n*extraLongFactorials(n-1) if n > 1 else 1
    fact = 1
    for i in range(n):
        fact = fact*n
        n -= 1
    return fact


print(extraLongFactorials(6))  # 720
print(extraLongFactorials(25))  # 15511210043330985984000000
print(extraLongFactorials(45))  # 119622220865480194561963161495657715064383733760000000000