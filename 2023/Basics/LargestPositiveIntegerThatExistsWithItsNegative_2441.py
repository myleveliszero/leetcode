# Status: Not Bad

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        if max(nums) < 0:
            return -1
        for i in range(len(nums)):
            imax = max(nums)
            nums.remove(imax)
            if ((-1)*imax in nums):
                return imax
        return -1

solve = Solution()
print(solve.findMaxK(nums = [-1,10,6,7,-7,1]))