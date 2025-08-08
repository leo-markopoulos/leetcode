def isAnagram(s, t):
    if len(s) != len(t):
        return False
        
    i = 0
    s = list(s)
    t = list(t)
    while t:
        if s[i] in t:
            t.remove(s[i])
        else:
            return False
        i += 1
    return True