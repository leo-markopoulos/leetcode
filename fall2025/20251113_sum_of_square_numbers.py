def judgeSquareSum(c):
    squares = []
    i = 0
    while i**2 <= c:
        squares.append(i**2)
        i += 1
    
    right = len(squares) - 1
    left = 0
    while left <= right:
        current = squares[left] + squares[right]
        if current == c:
            return True
        elif current < c:
            left += 1
        else:
            right -= 1

    return False
