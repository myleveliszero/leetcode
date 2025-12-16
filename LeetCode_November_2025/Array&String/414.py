from typing import *
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = nums[0]
        for i in nums:
            if i > first:
                first = i
        second = -2147483649
        for j in nums:
            if j > second and j!=first:
                second = j
        third = -2147483649
        for k in nums:
            if k > third and k!=first and k!=second:
                third = k
        if third!=second and third!=first and third!=-2147483649:
            return third
        else:
            return first

       
sol = Solution().thirdMax
print(sol(nums = [3,2,1]))
print(sol(nums = [1,2]))
print(sol(nums = [-500]))
print(sol(nums = [-500,500,-1000]))