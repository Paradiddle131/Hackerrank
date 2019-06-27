# k: cancellation threshold
# a: list of arrival times
# print YES if CANCELLED
def angryProfessor(k, a):
    countComers = 0
    for i in a:
        if i <= 0:
            countComers += 1
    if countComers >= k:
        return "NO"
    return "YES"

print(angryProfessor(3, [-1, -3, 4, 2]))  # YES
print(angryProfessor(2, [0, -1, 2, 1]))  # NO