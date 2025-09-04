def maxSubArray(nums):        
    best = min(nums)
    total = 0
    for n in nums:
        total += n
        best = max(best, total)
        if total < 0:
            total = 0

    return best