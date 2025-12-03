from collections import Counter


def minSetSize(arr):
    freqs = Counter(arr)
    counts = sorted(freqs.values(), reverse=True)
    
    total = 0
    result = 0 
    for count in counts:
        total += count
        result += 1
        if total >= len(arr) // 2:
            break
    
    return result