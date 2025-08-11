def largestPerimeter(nums):
    nums.sort()
    nums = nums[::-1]
    for i in range(len(nums) - 2):
        a, b, c = nums[i], nums[i+1], nums[i+2]
        if a < b + c:  
            return a + b + c
    return 0