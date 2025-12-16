from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hmap:
                return [i, hmap[diff]]
            hmap[nums[i]] = i

sol = Solution().twoSum
print(sol(nums = [2,7,11,15], target = 9))