def countPalindromicSubsequence(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = 0
    for c in letters:
        if s.count(c) >= 2:
            l = 0 
            while not s[l] == c:
                l += 1
            r = len(s) - 1 
            while not s[r] == c:
                r -= 1
            
            result += len(set(s[l+1:r]))
    
    return result