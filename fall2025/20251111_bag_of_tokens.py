def bagOfTokensScore(tokens, power):
    tokens.sort()
    result = 0
    left, right = 0, len(tokens) - 1
    current = 0
    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            current += 1
            left += 1
            result = max(result, current)
        elif current > 0:
            power += tokens[right]
            current -= 1
            right -= 1
        else:
            break
            
    return result