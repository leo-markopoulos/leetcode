def permute(nums):
    result = []
    current = []
    def backtrack():
        if len(current) == len(nums):
            result.append(current[:])
            return

        for num in nums:
            if num not in current:
                current.append(num)
                backtrack()
                current.pop()

    backtrack()
    return result