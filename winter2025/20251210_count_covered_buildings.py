def countCoveredBuildings(n, buildings):
    rmax, rmin = [0] * (n + 1), [n + 1] * (n + 1)
    cmax, cmin = [0] * (n + 1), [n + 1] * (n + 1)
    for x, y in buildings:
        rmax[y] = max(rmax[y], x)
        rmin[y] = min(rmin[y], x)
        cmax[x] = max(cmax[x], y)
        cmin[x] = min(cmin[x], y)

    result = 0
    for x, y in buildings:
        if rmin[y] < x < rmax[y] and cmin[x] < y < cmax[x]:
            result += 1

    return result