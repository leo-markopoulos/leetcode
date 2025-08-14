def largestNumber(nums):
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    
    def should_x_come_first(x, y):
        i = 0
        min_len = min(len(x), len(y))
        
        while i < min_len:
            if x[i] > y[i]:
                return True
            elif x[i] < y[i]:
                return False
            i += 1
        
        if len(x) == len(y):
            return False
        
        if len(x) > len(y):
            remaining = x[min_len:]
            return should_x_come_first(remaining, y)
        else:
            remaining = y[min_len:]
            return not should_x_come_first(remaining, x)
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if not should_x_come_first(nums[i], nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    
    if nums[0] == '0':
        return '0'
    
    return ''.join(nums)