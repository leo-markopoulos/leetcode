def constructRectangle(area):
    w = int(area ** 0.5)
    while area % w != 0:
        w -= 1
    l = area // w
    return [l, w]