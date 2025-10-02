def equalSubstring(s, t, maxCost):
    current_cost = 0
    result = 0
    left = 0
    for right in range(len(s)):
        if s[right] != t[right]:
            current_cost += abs(ord(s[right])-ord(t[right]))
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left])-ord(t[left]))
                left += 1
        
        result = max(result, right-left+1)
    return result