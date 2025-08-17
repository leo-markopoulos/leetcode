def convertToBase7(num):
    if num == 0: 
        return '0'
    negative = num < 0
    num = abs(num)
    result = []
    while num > 0:
        result.append(str(num % 7))
        num //= 7
    
    return '-' +  ''.join(reversed(result)) if negative else  ''.join(reversed(result))