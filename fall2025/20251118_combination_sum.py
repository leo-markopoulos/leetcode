from collections import deque

def combinationSum(candidates, target):
    res = []
    queue = deque()
    queue.append(([], 0, 0))  
    while queue:
        comb, curr_sum, start = queue.popleft()
        if curr_sum == target:
            res.append(comb)
            continue
            
        for i in range(start, len(candidates)):
            next_sum = curr_sum + candidates[i]
            if next_sum <= target:
                queue.append((comb + [candidates[i]], next_sum, i))

    return res