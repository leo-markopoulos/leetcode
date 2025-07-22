def addDigits(num):
    while num >= 10:
        digits = list(str(num))
        total = 0
        for i in digits:
            total += int(i)
            num = total
    return num