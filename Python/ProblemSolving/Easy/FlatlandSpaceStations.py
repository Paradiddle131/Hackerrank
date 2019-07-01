def flatlandSpaceStations(n, c):
    distances = []
    for city in range(n):
        for statcity in c:
            distances.append(abs(city - statcity))

    return max(distances)


print(flatlandSpaceStations([5, 2], [0, 4]))