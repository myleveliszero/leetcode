from typing import*
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
        hmap = dict()
        for val in nums1:
            if val in hmap:
                hmap[val] +=1
            else:
                hmap[val] = 1

        res = []
        for val in nums2:
            if val in hmap and hmap[val] > 0:
                res.append(val)
                hmap[val] -= 1

        return res

sol = Solution().intersect
print(sol(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(sol(nums1 = [14,23,5], nums2 = [9,4,9,8,4]))
print(sol(nums1 = [9,0,1], nums2 = [0,0,0,0,1]))