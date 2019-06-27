# a: rotation amount
# k: indices to return
def circularArrayRotation(a, k, queries):
    listblank = [None]*len(queries)
    listres = []
    for i in range(len(queries)):
        listblank[(i+a) % len(queries)] = queries[i]
    for j in range(len(listblank)):
        if j < len(k):
            listres.append(listblank[k[j]])
    return listres
# solved but hacerrank gives runtime error at line 7 (int + list)

print(circularArrayRotation(2, [1, 2], [1, 2, 3]))  # 3 1 (2 3 1)
print(circularArrayRotation(2, [1, 2], [3, 4, 5]))  # 5 3 (4 5 3)
print(circularArrayRotation(13, [2, 0, 3], [11, 9, 56, 7]))  # 9 7 56 (7 11 9 56)