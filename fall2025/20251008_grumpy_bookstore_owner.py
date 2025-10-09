def maxSatisfied(customers, grumpy, minutes):
    if minutes >= len(grumpy):
        return sum(customers)
    
    result = 0
    for i in range(len(customers)):
        if grumpy[i] == 0:
            result += customers[i]
            customers[i] = 0
    
    best = 0
    for i in range(len(customers)-minutes+1):
        best = max(best, sum(customers[i:i+minutes]))

    return result + best