def findMedianSortedArrays(nums1, nums2):
    nums3 = nums1 + nums2
    nums3.sort()
    n = len(nums3)

    if (n % 2 == 0) :
        return float((nums3[int(n/2)] + nums3[int(n/2)-1]))/2
    else :
        return nums3[(n//2)]

print(findMedianSortedArrays([1,2],[3,4]))
