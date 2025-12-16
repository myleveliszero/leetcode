from typing import*
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        left, right = 0, 0
        res = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                res.append(nums1[left])
                left, right = left+1, right+1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                left += 1

        return res
    
sol = Solution().intersect
print(sol(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(sol(nums1 = [14,23,5], nums2 = [9,4,9,8,4]))
print(sol(nums1 = [9,0,1], nums2 = [0,0,0,0,1]))