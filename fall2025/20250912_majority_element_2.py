def majorityElement(nums):
    nums.sort()
    result = []
    amt = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] in result:
            continue
        elif nums[right] == nums[left]:
            amt += 1
            if amt * 3 > len(nums):
                result.append(nums[left])
        else: 
            left = right
            amt = 1
            if amt * 3 > len(nums):
                result.append(nums[left])
    return result