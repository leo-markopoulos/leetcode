def numSub(s):
    count = 0
    current = 0
    for char in s:
        if char == '1':
            current += 1
            count += current
        else:
            current = 0

    return count % (10**9+7)