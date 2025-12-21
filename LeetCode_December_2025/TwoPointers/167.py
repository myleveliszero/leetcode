from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left]+nums[right] > target:
                right -= 1
            elif nums[left]+nums[right] < target:
                left += 1
            else:
                return (left+1, right+1)
            