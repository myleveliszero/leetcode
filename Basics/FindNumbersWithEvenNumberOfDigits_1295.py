# Status: Good

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """return how many of them contain an even number of digits."""
        return sum(len(str(i))%2==0 for i in nums)

solve = Solution()
print(solve.findNumbers(nums = [12,345,2,6,7896]))