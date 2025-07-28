def findMedianSortedArrays(nums1, nums2):
    i = 0
    j = 0
    nums3 = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1

    nums3 += nums1[i:]
    nums3 += nums2[j:]

    i = len(nums3)
    if i % 2 == 1:
        return nums3[i // 2]
    else:
        return (nums3[i // 2 - 1] + nums3[i // 2]) / 2