def wateringPlants(plants, capacity):
    result = 0
    c = capacity
    for i, p in enumerate(plants):
        if c >= p:
            c -= p
            result += 1
        else:
            c = capacity
            result += 2*i+1
            c -= p
    return result