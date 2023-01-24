# Status: Good

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mn, mx = min(nums), max(nums)
        while mn != mx:
            if mn > mx:
                mn -= mx
            else:
                mx -= mn
        return mn
    def version2(self, nums):
        import math
        return math.gcd(min(nums), max(nums))

solve = Solution()
print(solve.findGCD(nums = [2,5,6,9,10]))
print(solve.findGCD(nums = [230, 10,30,23]))
print(solve.version2(nums = [2,5,6,9,10]))
print(solve.version2(nums = [230, 10,30,23]))