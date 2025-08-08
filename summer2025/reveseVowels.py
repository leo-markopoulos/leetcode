def reverseVowels(s):
    s = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] in 'aeiouAEIOU' and s[j] in 'aeiouAEIOU':
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        else:
            if s[i] not in 'aeiouAEIOU':
                i += 1
            if s[j] not in 'aeiouAEIOU':
                j -= 1 
    return ''.join(s)