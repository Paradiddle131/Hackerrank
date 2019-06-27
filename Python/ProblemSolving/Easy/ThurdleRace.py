#k: initial maximum height Dan can jump
#height: array of hurdle heights
#determine the minimum number of doses Dan must take to be able to clear all the hurdles in the race.
def hurdleRace(k, height):
    return max(height)-k if max(height)-k>0 else 0
print(hurdleRace(4, [1, 6, 3, 5, 2])) #2
print(hurdleRace(7, [2, 5, 4, 5, 2])) #0