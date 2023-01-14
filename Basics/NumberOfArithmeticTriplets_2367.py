# Status: Bad

class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        answ = 0
        nlen = len(nums)
        for i in range(nlen):
            for j in range(i+1, nlen):
                if nums[j]-nums[i] != diff:
                    continue
                for k in range(j+1, nlen):
                    if nums[j]-nums[i] == diff and nums[k]-nums[j]==diff:
                        answ += 1
        return answ

solve = Solution()
print(solve.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))
print(solve.arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))