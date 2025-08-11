def hammingDistance(x, y):
    xbin = []
    i = 1
    while i <= x:
        i *= 2
    i //= 2
    while i > 0:
        if x >= i:
            xbin.append('1')
            x -= i
        else:
            xbin.append('0')
        i //= 2
    
    ybin = []
    i = 1
    while i <= y:
        i *= 2
    i //= 2
    while i > 0:
        if y >= i:
            ybin.append('1')
            y -= i
        else:
            ybin.append('0')
        i //= 2
    
    result = 0
    if len(ybin) > len(xbin):
        xbin, ybin = ybin, xbin
    
    for i in range(len(xbin) - len(ybin)):
        if xbin[i] == '1':
            result += 1
    
    for i in range(len(ybin)):
        if xbin[-(len(ybin)-i)] != ybin[i]:
            result += 1
    
    return result
