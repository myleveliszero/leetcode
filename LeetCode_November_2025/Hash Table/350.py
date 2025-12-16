from typing import*
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap1, hmap2 = dict(), dict()
        for val in nums1:
            if val in hmap1:
                hmap1[val] += 1
            else:
                hmap1[val] = 1
        for val in nums2:
            if val in hmap2:
                hmap2[val] += 1
            else:
                hmap2[val] = 1
        res = []
        for key in hmap1.keys():
            if key in hmap2:
                for i in range(min(hmap1[key], hmap2[key])):
                    res.append(key)

        return res
    
sol = Solution().intersect
print(sol(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(sol(nums1 = [14,23,5], nums2 = [9,4,9,8,4]))
print(sol(nums1 = [9,0,1], nums2 = [0,0,0,0,1]))