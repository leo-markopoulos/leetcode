def maxOperations(s):
    if '1' not in s or '0' not in s:
        return 0 

    if s[-1] == '1':
        last_is_one = True
    else:
        last_is_one = False

    ones = []
    current = 0 
    for i in range(len(s)):
        if s[i] == '1':
            current += 1
            if i == len(s)-1:
                ones.append('1'*current)
                current = 0

        elif current:
            ones.append('1'*current)
            current = 0
    
    result = 0
    for i in range(len(ones)-1):
        result += len(ones[i])
        ones[i+1] += ones[i]
    
    return result + (not last_is_one) * len(ones[-1])