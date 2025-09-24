def maxWidthRamp(nums):
    stack = [0]
    for i in range(1,len(nums)):
        if nums[stack[-1]] > nums[i]:
            stack.append(i)
    
    result = 0
    for j in range(1,len(nums)+1):
        while stack and nums[stack[-1]] <= nums[len(nums)-j]:
            result = max(result, len(nums) - j - stack.pop())
    
    return result