import math
def viralAdvertising(n):
    share = 0
    cumLike = 0
    like = 5/3
    for i in range(n):
        share = 3*like
        like = math.floor(share/2)
        # if i == 0:
        #     like = 0
        cumLike += like
    return cumLike


print(viralAdvertising(3))  # 9
print(viralAdvertising(4))  # 15
print(viralAdvertising(5))  # 24
