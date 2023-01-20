# Status: Good

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums, answ = sorted(nums), 0
        for i in range(len(nums)//2):
            pairsum = nums[i] + nums[~i]
            if  pairsum > answ:
                answ = pairsum
        return answ

solve = Solution()
print(solve.minPairSum(nums = [3,5,2,3]))
