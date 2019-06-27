def migratoryBirds(arr):
    type=[0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
            type[arr[i]] += 1
    return type.index(max(type))

print(migratoryBirds([1, 4, 4, 4, 5, 3]))
