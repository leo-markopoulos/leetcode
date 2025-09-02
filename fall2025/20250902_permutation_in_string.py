def checkInclusion(s1, s2):
    key = {i: s1.count(i) for i in s1}
    left = 0
    for right in range(len(s2)):
        if s2[right] in key:
            key[s2[right]] -= 1
            while key[s2[right]] < 0: 
                key[s2[left]] += 1
                left += 1
        else:
            key = {i: s1.count(i) for i in s1}
            left = right + 1 

        if sum(key.values()) == 0: 
            return True
                
    return False