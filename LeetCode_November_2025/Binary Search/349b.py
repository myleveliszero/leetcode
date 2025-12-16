from typing import*
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binSearch(nums, target) -> bool:
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right-left)//2 
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right -= 1
                else:
                    left += 1
                
            return False
        res = set()
        nums1.sort()
        for i in range(len(nums2)):
            if binSearch(nums1, nums2[i]):
                res.add(nums2[i])

        return list(res)
    
sol = Solution().intersection
print(sol(nums1 = [1,2,2,1], nums2 = [2,2]))
print(sol(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
