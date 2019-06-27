def permutationEquation(p):
    sortedList = sorted(p)
    listRes = []
    for i in sortedList:
        listRes.append(p.index(p.index(i)+1)+1)
    return listRes


print(permutationEquation([5, 2, 1, 3, 4]))  # [4, 2, 5, 1, 3]
print(permutationEquation([2, 3, 1]))  # [2, 3, 1]
print(permutationEquation([4, 3, 5, 1, 2]))  # [1, 3, 5, 4, 2]
