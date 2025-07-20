def isPowerOfThree(n):
    x = 0
    while True:
        if 3**x >= n:
            if 3**x == n:
                return True
            else: return False
        x += 1