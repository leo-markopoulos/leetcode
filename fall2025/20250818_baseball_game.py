def calPoints(operations):
    result = []
    for i in operations:
        if i == '+':
            result.append(result[-1]+result[-2])
        elif i == 'D': 
            result.append(result[-1]*2)
        elif i == 'C':
            result = result[:-1]
        else:
            result.append(int(i))             
    return sum(result)
