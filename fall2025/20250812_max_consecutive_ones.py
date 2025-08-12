def findMaxConsecutiveOnes(nums):
    result = 0
    x = 0
    for i in nums:
        if i == 1:
            x += 1
        else:
            x = 0
        result = max(result,x)
    return result