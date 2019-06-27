def utopianTree(n):
    height = 1
    switch = 0
    for i in range(n):
        if switch == 0:
            height *= 2
        else:
            height += 1
        switch += 1
        if switch == 2:
            switch -= 2
    return height

print(utopianTree(0))  # 1
print(utopianTree(1))  # 2
print(utopianTree(4))  # 7
# print(utopianTree([0, 1]))  # 1 2
