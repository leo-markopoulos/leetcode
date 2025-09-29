def numberOfAlternatingGroups(colors, k):
    if k > len(colors):
        return 0
    
    colors += colors[:k-1]
    result = 0
    left = 0
    for right in range(1,len(colors)):
        if colors[right-1] == colors[right]:
            left = right
        elif right - left + 1 >= k:
            left += 1
            result += 1

    return result