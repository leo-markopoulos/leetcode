def majorityElement(nums):
    elements = {}
    for i in nums:
        if not i in elements:
            elements.update({i:1})
        else:
            elements[i] += 1
    return max(elements, key=elements.get)