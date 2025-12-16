# Status: Not Bad

class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] != nums[j]:
                    for k in range(j+1, len(nums)):
                        if nums[i] != nums[k] and nums[j] != nums[k]:
                            cnt += 1
        return cnt

solve = Solution()
print(solve.unequalTriplets(nums = [4,4,2,4,3]))