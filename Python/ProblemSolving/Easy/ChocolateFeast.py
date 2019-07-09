def chocolateFeast(n, c, m):
    count = 0
    wrapper = n / c
    newChocolate = 0
    while wrapper > m:
        newChocolate, wrapper = divmod(wrapper, m)
        wrapper += newChocolate
    return n/c + newChocolate


print(chocolateFeast(15, 3, 2))  # 9 bars