def nonDivisibleSubset(k, S):
    listSums = []
    dividibles = set()
    for i in S:
        for j in S[1:]:
            if i != j & j > i:
                listSums.append(i+j)
                if divmod(i+j, k)[1] is not 0:
                    dividibles.add(i)
                    dividibles.add(j)
    print(listSums)
    print(dividibles)
    print()
    return len(dividibles)


print(nonDivisibleSubset(3, [1, 7, 2, 4])) # [8, 3, 5, 9, 6, 11] - {1, 4, 7}
print(nonDivisibleSubset(4, [1, 3, 7, 6, 4, 2])) # [4, 8, 7, 5, 3, 10, 9, 7, 13, 11, 10, 5, 9, 8, 6] -
print(nonDivisibleSubset(9, [422346306, 940894801, 696810740, 862741861, 85835055, 313720373])) # 5

# S.index(j)>S.index(i)