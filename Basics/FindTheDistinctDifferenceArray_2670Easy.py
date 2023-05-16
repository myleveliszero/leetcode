class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            left = len(set(nums[:i+1]))
            right = len(set(nums[i+1:]))
            ans.append(left-right)
        return ans

solve = Solution()
print(solve.distinctDifferenceArray([1,2,3,4,5]))