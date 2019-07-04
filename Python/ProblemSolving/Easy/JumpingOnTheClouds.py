def jumpingOnClouds(c):
    count = 0
    for i in range(len(c)):
        if c[i] != 1:
            try:
                if c[i] == 0 and c[i+1] == 0 and c[i+2] == 0:
                    count += 1
                    c[i+1] = 1
                elif (c[i] == 0 and c[i+1] == 1 and c[i+2] != -1) or (c[i] == 0 and c[i+1] == 0 and c[i+2] == 1):
                    count += 1
            except:
                if i == len(c)-2 and c[i+1] == 0:
                    count += 1
                    break
                elif i == len(c)-2 and c[i+1] == 1:
                    break
                elif i == len(c)-1:
                    break
                continue
    return count


print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))  # 3
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # 4
print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))  # 3
print(jumpingOnClouds([0, 0, 0, 0, 0, 1, 0]))  # 3
print(jumpingOnClouds([0, 0, 0, 0, 0, 1, 0, 0, 0]))  # 4
print(jumpingOnClouds([0, 0, 0, 0, 0, 1, 0, 0, 0, 0]))  # 5
print(jumpingOnClouds([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]))  # 5
print(jumpingOnClouds([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]))  # 6
