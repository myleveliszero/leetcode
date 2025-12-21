from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        
sol = Solution().findDuplicate
print(sol([1,3,4,2,2]))
print(sol([3,1,3,4,2]))
print(sol([3,3,3,3,3]))
        
        
