def minimumDistances(a):
    dictIndexes = {}
    dupCount = 0
    for number in range(10):
        for (key, value) in enumerate(a):
            if value == number:
                dictIndexes['{}'.format(value)] = key
                dictIndexes.update({'{}'.format(value): list(dictIndexes.values())[] + key})
    return dictIndexes

print(minimumDistances([7, 1, 3, 4, 1, 7]))  # 3 (4-1)