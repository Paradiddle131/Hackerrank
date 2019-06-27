"""
length of the segment matches Ron's birth month
sum of the integers on the squares is equal to his birth day
determine how many ways she can divide the chocolate.

s: an array of integers, the numbers on each of the squares of chocolate
d: an integer, Ron's birth day
m: an integer, Ron's birth month

1 2 1 3 2
3 2
= 2

2 1 1 3 2
4 2
= 2

4
4 1
= 1
"""
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if i < len(s):
            if sum(s[i:i+m]) == d:
                count += 1
    return count




print(birthday([1, 2, 1, 3, 2], 3, 2))