def removeStars(s):
    result = []
    for c in s:
        if c == '*':
            result.pop()
        else:
            result.append(c)

    return ''.join(result)