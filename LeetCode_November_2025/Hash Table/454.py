from typing import*
from itertools import *
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hmap = dict()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ab = nums1[i]+nums2[j]
                if ab in hmap:
                    hmap[ab] += 1
                else:
                    hmap[ab] = 1

        cnt = 0
        for c in nums3:
            for d in nums4:
                if -(c+d) in hmap:
                    cnt += hmap[-(c+d)]
                    
        return cnt  

sol = Solution().fourSumCount
print(sol([0, 0],[0, 0],[0, 0],[0, 0]))