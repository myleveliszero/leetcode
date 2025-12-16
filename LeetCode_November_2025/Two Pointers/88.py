def merge(nums1, m, nums2, n: int) -> None:
    nums3 = []
    l, r = 0, 0
    while l+r < m+n:
        if l==m:
            nums3.append(nums2[r])
            r += 1
        elif r==n:
            nums3.append(nums1[l])
            l += 1
        elif nums1[l] <= nums2[r]:
            nums3.append(nums1[l])
            l += 1
        else:
            nums3.append(nums2[r]) 
            r += 1
    for i in range(len(nums1)):
        nums1[i] = nums3[i]
    print(nums1)


merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

