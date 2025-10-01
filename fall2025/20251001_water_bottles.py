def numWaterBottles(numBottles, numExchange):
    result = numBottles
    while numBottles >= numExchange:
        result += numBottles // numExchange
        numBottles = numBottles % numExchange + numBottles // numExchange
    return result   