# Status: Not Bad

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        digits = []
        for i in nums:
            for j in str(i):
                digits.append(int(j))
        return digits
    
solve = Solution()
print(solve.separateDigits(nums = [13,25,83,77]))