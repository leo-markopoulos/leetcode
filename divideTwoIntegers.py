def divide(dividend, divisor):
    if dividend == -2147483648 and divisor == -1:
        return 2147483647

    n = (dividend < 0) != (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    result = 0

    while dividend >= divisor:
        temp = divisor
        multiple = 1

        
        while dividend >= temp + temp:
            temp = temp + temp     
            multiple = multiple + multiple  

        dividend = dividend - temp
        result = result + multiple

    if n:
        result = -result

    if result < -2147483648:
        return -2147483648
    if result > 2147483647:
        return 2147483647

    return result