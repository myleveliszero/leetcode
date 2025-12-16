from typing import*
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort() 
        nums2.sort()
        i, j, res = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if not res:
                    res.append(nums1[i])
                if res and res[-1] != nums1[i]:
                    res.append(nums1[i])
                i, j = i+1, j+1
        return res
    
sol = Solution().intersection
print(sol(nums1 = [1,2,2,1], nums2 = [2,2]))
