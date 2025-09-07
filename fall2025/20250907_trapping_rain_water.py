def trap(height):
    result = 0
    left = 0
    for right in range(len(height)):
        if height[right] >= height[left]:
            for i in range(left + 1, right):
                result += height[left] - height[i]
            left = right

    if left < len(height) - 1:
        right = len(height) - 1
        for left in range(len(height) - 1, left - 1, -1):
            if height[left] >= height[right]:
                for i in range(right - 1, left, -1):
                    result += height[right] - height[i]
                right = left

    return result