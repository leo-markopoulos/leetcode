def longestPalindrome(s):
    result = ''
    for i in range(len(s)):

        j = 0
        while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
            if 2 * j + 1 > len(result):
                result = s[i - j:i + j + 1]
            j += 1

        j = 0
        while i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
            if 2 * j + 2 > len(result):
                result = s[i - j:i + j + 2]
            j += 1

    return result