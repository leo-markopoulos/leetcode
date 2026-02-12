def longestString(x, y, z):
    result = z*2
    n = min(x,y)
    result += n*4 
    x -= n
    y -= n
    if x > 0 or y > 0:
        result += 2
    return result