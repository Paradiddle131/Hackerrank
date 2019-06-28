# parts = [['h', 'a', 'v', 'e'], ['a', 'n', 'i', 'c'], ['e', 'd', 'a', 'y']]
# parts = [['f', 'e', 'e', 'd'], ['t', 'h', 'e', 'd'], ['o', 'g']]
# for x, y, z in zip(*parts):
#     print(x, y, z)
# print("-----")
#
# string3 = ""
# listPicked = []
# for i in range(len(parts)+1):
#     for x in parts:
#         if i < len(x[i]):
#             pass
#         else:
#             print(x[i], end ='')
#             string3 += x[i]
#             listPicked.append(x[i])
#             if x == parts[len(parts)-1]:
#                 listPicked.append(x[i])
#                 string3 += " "
# print("\nlistPicked: ", listPicked)
# print("string3: ", string3)

# def makeGreatAgain(list):
#     listRes = [None]*len(list)
#     if list[0] != max(list):
#         list[0], list[list.index(min(list[1:]))] = \
#             list[list.index(min(list[1:]))], list[0]
#     else:
#         if  > list[0]
#     listRes[0] = list[0]
#     for i in sorted(list[1:]):
#         listRes[sorted(list[1:]).index(i)+1] = i
#     return listRes

# print(makeGreatAgain([104, 101, 102, 103]))
# print(makeGreatAgain([100, 107, 104, 99]))
# print(makeGreatAgain([97,  100, 98,  102]))

def findFirstLarger(num, sortedList):
    '''Finds the smallest index in the sortedList
    of the element which is greater-than or equal to num'''

    slen = len(sortedList)
    start = 0

    while slen > 0:
        m = start + slen//2

        if sortedList[m] < num:
            slen = slen - (m+1 - start)
            start = m+1
            continue

        if start < m and sortedList[m-1] > num:
            slen = m - start
            continue

        return sortedList[m]

    raise ValueError('Not found')

sortedList=[n*2 for n in range(131072)]
print(findFirstLargerOrEqual(262139, sortedList)) #output: 262140
print(findFirstLargerOrEqual(100, sorted([100, 107, 104, 99])))  # 104
