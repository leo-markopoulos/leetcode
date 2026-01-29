def beautifulIndices(s, a, b, k):
    result = []
    ind1, ind2 = [], []
    for i in range(len(s) - len(a) + 1):
        if s[i:i+len(a)] == a:
            ind1.append(i)

    for j in range(len(s) - len(b) + 1):
        if s[j:j+len(b)] == b:
            ind2.append(j)
    
    for i in ind1:
        for j in ind2:
            if abs(i - j) <= k:
                result.append(i)
                break   

    result.sort()
    return result