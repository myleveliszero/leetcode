# Status: Not Bad

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[2*i] for i in range(len(nums)//2))
    def version2(self, nums):
        return sum(sorted(nums)[::2])


solve = Solution()
print(solve.arrayPairSum(nums = [1,4,3,2]))
print(solve.arrayPairSum(nums = [6,2,6,5,1,2]))
print(solve.version2(nums = [1,4,3,2]))
print(solve.version2(nums = [6,2,6,5,1,2]))