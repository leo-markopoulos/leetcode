import collections

def find132pattern(nums):
    if len(nums) < 3:
        return False
    stack = collections.deque()        
    s2 = float('-inf') 
    for i in range(len(nums) - 1, -1, -1):
        s1 = nums[i]
        if s1 < s2:
            return True
    
        while stack and stack[-1] < s1:
            s2 = stack.pop()            
        stack.append(s1)

    return False