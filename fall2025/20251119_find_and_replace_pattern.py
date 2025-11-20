def findAndReplacePattern(words, pattern):
    letters = 'abcdefghijklmnopqrstuvwyz'
    letter_map = {}
    i = 0
    p = ''
    for c in pattern:
        if not c in letter_map:
            letter_map[c] = letters[i]
            i += 1
        p += letter_map[c]
    
    result = []
    for s in words:
        letter_map = {}
        i = 0
        p2 = ''
        for c in s:
            if not c in letter_map:
                letter_map[c] = letters[i]
                i += 1
            p2 += letter_map[c]
        if p2 == p:
            result.append(s)
    
    return result