from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [nums[0]]
        post_prod = [0]*len(nums)
        post_prod[-1] = nums[-1]
        for i in range(1, len(nums)):
            pre_prod.append(pre_prod[-1] * nums[i])
            post_prod[len(nums)-1-i] = post_prod[len(nums)-i] * nums[len(nums)-1-i]
        
        ans = [0]*len(nums)
        for i in range(len(nums)):
            a = pre_prod[i-1] if i > 0 else 1
            b = post_prod[i+1] if i < len(nums)-1 else 1
            ans[i] = a*b
        
        return ans
    

print(Solution().productExceptSelf([1,2,3,4]))