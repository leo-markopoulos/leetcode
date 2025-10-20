def finalValueAfterOperations(operations):
    key = {"++X" : 1, "X++" : 1, "--X" : -1, "X--" : -1}
    result = 0
    for op in operations:
        result += key[op]
    return result