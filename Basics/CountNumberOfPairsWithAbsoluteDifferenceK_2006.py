# Status: Not Bad

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        answ = 0
        nlen = len(nums)
        for i in range(nlen):
            for j in range(i+1, nlen):
                if abs(nums[i]-nums[j]) == k:
                    answ += 1
        return answ

solve = Solution()
print(solve.countKDifference(nums = [1,2,2,1], k = 1))
print(solve.version2(nums = [1,2,2,1], k = 1))