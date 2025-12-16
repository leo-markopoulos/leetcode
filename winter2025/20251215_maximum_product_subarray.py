def maxProduct(nums):
    result = max(nums)
    c_max, c_min = 1, 1 
    for num in nums:
        temp = c_max * num
        c_max = max(temp, c_min * num, num)
        c_min = min(temp, c_min * num, num)
        result = max(result, c_max)
    
    return result