class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    return nums1[i]
                elif nums1[i] < nums2[j]:
                    break
        return -1
