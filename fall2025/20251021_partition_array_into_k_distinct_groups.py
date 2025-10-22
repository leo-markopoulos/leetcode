def partitionArray(nums, k):
    if len(nums) % k != 0:
        return False
    
    freq = {}
    groups = len(nums) // k
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    if any(count > groups for count in freq.values()):
        return False
    else:
        return True