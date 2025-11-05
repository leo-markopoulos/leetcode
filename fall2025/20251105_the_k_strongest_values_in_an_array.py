def getStrongest(arr, k):
    arr.sort()
    m = arr[(len(arr)-1)//2]
    result = []
    left = 0
    right = len(arr) - 1
    while len(result) < k:
        if abs(arr[left]-m) > abs(arr[right]-m) or arr[left] > arr[right]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right])
            right -= 1
    return result