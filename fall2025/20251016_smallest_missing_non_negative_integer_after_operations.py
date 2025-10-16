def findSmallestInteger(nums, value):
    freq = [0] * value
    for num in nums:
        r = num % value
        freq[r] += 1
    
    full_loops = 0
    while True:
        for i in range(len(freq)):
            if freq[i] == 0:
                return full_loops*value + i
            else: 
                freq[i] -= 1

        full_loops += 1