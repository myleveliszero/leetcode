from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for idx, val in enumerate(nums):
            hmap[val] = idx
        
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hmap and i!=hmap[diff]:
                return [i, hmap[diff]]
        
sol = Solution().twoSum
print(sol(nums = [2,7,11,15], target = 9))