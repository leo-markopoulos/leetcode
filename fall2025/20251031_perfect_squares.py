from collections import deque

def numSquares(n):
    squares = []
    i = 1
    while i ** 2 <= n:
        squares.append(i**2)
        i += 1

    if n in squares:
        return 1
    
    result = n 
    queue = deque([(num, 1) for num in squares])
    while queue:
        val, i = queue.popleft()
        if n - val in squares:
            return i + 1
        for sq in squares:
            if sq + val < n:
                queue.append((sq+val, i+1))
            else:
                continue      

    return result