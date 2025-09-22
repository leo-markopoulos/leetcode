def pancakeSort(arr):
    result = []
    for size in range(1, len(arr) + 1):
        end = len(arr) - size
        max_index = arr.index(max(arr[:end + 1]))
        if max_index == end:
            continue
        if max_index != 0:
            result.append(max_index + 1)
            arr[:max_index + 1] = reversed(arr[:max_index + 1])
        result.append(end + 1)
        arr[:end + 1] = reversed(arr[:end + 1])

    return result
