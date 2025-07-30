def findLHS(nums):
    result = 0
    for num in set(nums):
        if num + 1 in nums:
            result = max(result, nums.count(num) + nums.count(num + 1))
    return result