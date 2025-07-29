def convert(s, numRows):
    if numRows == 1:
        return s
    result = ""
    step = 2 * (numRows - 1)
    for i in range(numRows):
        j = i
        while j < len(s):
            result += s[j]
            if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    result += s[j + step - 2 * i]
            j += step
    return result