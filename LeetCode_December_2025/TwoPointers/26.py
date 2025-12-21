from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                nums[left+1] = nums[right]
                left += 1
        return left + 1

    def removeDuplicates_2(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[left-1] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left 