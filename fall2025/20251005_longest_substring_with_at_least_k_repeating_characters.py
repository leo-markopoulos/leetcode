def longestSubstring(s, k):
    substrings = [s]
    result = 0
    while any(len(sub) >= k for sub in substrings):
        new_substrings = []
        for sub in substrings:
            if len(sub) < k or len(sub) < result:
                continue
            valid = True
            for char in set(sub):
                if sub.count(char) < k:
                    new_substrings.extend(sub.split(char))
                    valid = False
                    break
            if valid:
                result = max(result, len(sub))
        substrings = new_substrings

    return result