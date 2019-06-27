import math
#6 2
#= 1
def pageCount(n, p):
    if n == 1:
        return 0
    if n == 2 and p == 1:
        return 0
    if n%2 == 0 and n-p == 1:
        return 1
    start = p/2
    #print("From the beginning: " + start + " pages to turn to reach page #" + p)
    end = n/2 - p/2
    #print("From end: " + end + " pages to reach page #" + p)

    return int(min(start,end))

print(pageCount(2,1))
