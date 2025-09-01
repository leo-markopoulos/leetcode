def numMovesStones(a, b, c):
    return [0 if max(a,b,c)-min(a,b,c)==2 else 1 if max(a,b,c)-sorted([a,b,c])[1]<=2 or sorted([a,b,c])[1]-min(a,b,c)<=2 else 2, max(a,b,c)-min(a,b,c)-2]    