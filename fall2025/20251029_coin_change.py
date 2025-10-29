from collections import deque

def coinChange(coins, amount): 
    if amount == 0:
        return 0

    queue = deque([(0, 0)]) 
    visited = {0}   
    while queue:
        current_amount, num_coins = queue.popleft()
        for coin in coins:
            new_amount = current_amount + coin  

            if new_amount == amount:
                return num_coins + 1     

            elif new_amount < amount and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))
    
    return -1