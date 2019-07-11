def chocolateFeast(n, c, m):
    count = 0
    wrapper = n / c
    while wrapper >= m:
        newChocolate, wrapper = divmod(wrapper, m)
        wrapper += newChocolate
        count += newChocolate
    return int(count + n/c)


print(chocolateFeast(15, 3, 2))  # 9 bars
print(chocolateFeast(10, 2, 5))  # 6 bars
print(chocolateFeast(12, 4, 4))  # 3 bars
print(chocolateFeast(6, 2, 2))  # 5 bars