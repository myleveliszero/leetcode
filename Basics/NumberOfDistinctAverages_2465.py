# Status: Not Bad

class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        avg = set()
        while nums:
            avg.add((max(nums)+min(nums)))
            nums.remove(max(nums))
            nums.remove(min(nums))
        return len(avg)

solve = Solution()
print(solve.distinctAverages(nums = [4,1,4,0,3,5]))