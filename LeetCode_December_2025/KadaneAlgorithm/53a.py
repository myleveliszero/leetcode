# from typing import List 
# class Solution:    
#     def maxSubArray(self, nums: List[int]) -> int:
#         def dc(nums, left, right, max_sum):
#             if right - left == 0:
#                 return nums[left]
            
#             mid = (left+right)//2

#             left_sum = dc(nums, left, mid, max_sum)
#             if left_sum > max_sum[0]:
#                 max_sum[0] = left_sum
            
#             right_sum = dc(nums, mid+1, right, max_sum)
#             if right_sum > max_sum[0]:
#                 max_sum[0] = right_sum
            
#             return right_sum
        
#         max_sum = [nums[0]]
#         dc(nums, 0, len(nums)-1, max_sum)
        
#         return max_sum.pop()
    
# sol3 = Solution().maxSubArray

# print(sol3([-1, 10, -1, 3, 6, 5, -4]))
# print(sol3([-1, 10, -1, 3, 6, 5, -4]) == 23)
