def howManyGames(p, d, m, s):
    count = -1
    while s >= 0:
        s -= max(p, m)
        p -= d
        count += 1
    return max(0, count)


    # count = -1
    # total = 0
    # while p >= m:
    #     total += p
    #     count += 1
    #     # p = p - d if p - d > m else m
    #     if total > s:
    #         return count
    #     else:
    #         continue
    # return count



print(howManyGames(20, 3, 6, 80))  # 6