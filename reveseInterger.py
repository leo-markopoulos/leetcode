def reverse(x):
    if x == 0:
        return 0

    x = int(int(str(abs(x))[::-1]) *  x / abs(x))
    if not -2**31 <= x <= 2**31 - 1:
        return 0
    else:
        return x