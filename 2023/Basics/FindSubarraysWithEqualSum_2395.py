# Status: Not Bad

class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        pairssum = []
        for i in range(len(nums)-1):
            cursum = nums[i]+nums[i+1]
            if cursum in pairssum:
                return True
            else:
                pairssum.append(cursum)
        return False 
        
solve = Solution()
print(solve.findSubarrays(nums = [4,2,4]))
print(solve.findSubarrays(nums = [1,2,3,4,5]))