def longestPalindrome(s):
    letters = {}
    s = list(s)
    for i in range(len(s)):
        if not s[i] in letters:
            letters.update({s[i]:1})
        else:
            letters[s[i]] += 1
    result = 0
    isOdd = 0
    for i in letters.values():
        result += i - (i % 2)
        if isOdd == 0 and i % 2 == 1:
            isOdd += 1    
    return result + isOdd
