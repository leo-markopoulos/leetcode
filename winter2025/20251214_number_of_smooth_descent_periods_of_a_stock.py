def getDescentPeriods(prices):
    result = 0
    count = 1
    for i in range(1, len(prices)):
        if prices[i - 1] - prices[i] == 1:
            count += 1
        else:
            result += (count * (count + 1)) // 2
            count = 1
    result += (count * (count + 1)) // 2
    return result