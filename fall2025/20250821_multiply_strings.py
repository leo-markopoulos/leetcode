def multiply(num1, num2):
    num1, num2 = list(num1)[::-1], list(num2)[::-1]
    result = [0] * (len(num1) + len(num2))
    
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i+j] += int(num1[i]) * int(num2[j])
            result[i+j+1] += result[i+j] // 10
            result[i+j] %= 10
            
    while len(result) > 1 and result[-1] == 0:
        result.pop()
        
    return ''.join([str(x) for x in result[::-1]])