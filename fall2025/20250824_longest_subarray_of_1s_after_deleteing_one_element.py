def longestSubarray(nums):
    if 0 not in nums:
        return len(nums) - 1

    opts = []
    for i, char in enumerate(nums):
        if char == 0:
            opts.append(i)
    
    result = 0
    for i in range(len(opts)): 
        j = 0
        left, right = opts[i] - 1, opts[i] + 1
        while left >= 0 and nums[left] == 1:
            j += 1
            left -= 1
        while right < len(nums) and nums[right] == 1:
            j += 1
            right += 1
        result = max(result, j)    
                
    return result