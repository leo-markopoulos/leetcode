def characterReplacement(s, k):
    chars = {}
    left = 0
    result = 0
    for right in range(len(s)):
        if s[right] not in chars:
            chars.update({s[right]:1})
        else:
            chars[s[right]] += 1
        
        while sum(chars.values()) - max(chars.values()) > k:
            chars[s[left]] -= 1
            left += 1

        result = max(result, right-left+1)
    return result 