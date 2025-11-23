from collections import deque, Counter

def numTilePossibilities(tiles):
    result = set()        
    queue = deque([("", Counter(tiles))])
    while queue:
        current, leftover = queue.popleft()            
        for c in leftover:
            if leftover[c] > 0 and current + c not in result:
                    result.add(current + c)
                    new_leftover = leftover.copy()
                    new_leftover[c] -= 1
                    queue.append((current + c, new_leftover))
    
    return len(result)