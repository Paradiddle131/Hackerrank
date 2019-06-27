def catAndMouse(x, y, z):
    if abs(x-z) < abs(y-z):
        return "Cat A"
    elif abs(x-z) > abs(y-z):
        return "Cat B"
    else:
        return "Mouse C"
    #return "Cat A" if abs(x-z) < abs(y-z) else "Cat B" if abs(x-z) == abs(y-z) else "Mosue C"
catAndMouse(1, 2, 3) # Cat B
catAndMouse(1, 3, 2) # Mouse C
