def jump(nums):
    result = 0
    left = 0
    right = 0
    while right < len(nums) - 1:
        best_jump = 0
        for i in range(left, right+1):
            best_jump = max(i + nums[i], best_jump)
        left = right + 1
        right = best_jump
        result += 1
    
    return result  