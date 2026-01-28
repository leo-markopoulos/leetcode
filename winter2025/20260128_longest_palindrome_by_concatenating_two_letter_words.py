from collections import Counter

def longestPalindrome(words):
    freq = Counter(words)
    result = 0
    mid = False

    for word in list(freq.keys()):
        rev = word[::-1]
        if word == rev:
            pairs = freq[word] // 2
            result += pairs * 4
            freq[word] -= pairs * 2
            if freq[word] == 1:
                mid = True
        else:
            if rev in freq:
                pairs = min(freq[word], freq[rev])
                result += pairs * 4
                freq[word] -= pairs
                freq[rev] -= pairs

    if mid:
        result += 2

    return result