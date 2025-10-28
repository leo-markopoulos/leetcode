def minimumOperationsToMakeKPeriodic(word, k):
    count = {}
    for i in range(0, len(word), k):
        sub_str = word[i:i+k]
        if sub_str in count:
            count[sub_str] += 1
        else:
            count[sub_str] = 1
    
    return len(word)//k - max(count.values())