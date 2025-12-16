from typing import List
#Bucket Sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        memo = [0,0,0]
        for i in range(len(nums)):
            memo[nums[i]] += 1
        i = 0 
        for k in range(len(memo)):
            for _ in range(memo[k]):
                nums[i] = k
                i += 1
            