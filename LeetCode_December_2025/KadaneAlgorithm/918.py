# # didn't solved yet
# from typing import List
# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        
#         return


#     def brute_force(self, nums: List[int]) -> int:
#         def kadane_circle(nums, idx):
#             cur_sum = max_sum = nums[idx]
#             start = idx
#             for i in range(idx+1, len(nums)*2):
#                 if cur_sum <= 0:
#                     if i >= len(nums):
#                         break
#                     cur_sum = nums[i]
#                     start = i
#                 else:
#                     if start == i % len(nums):
#                         break
#                     cur_sum += nums[i % len(nums)]
#                 if cur_sum > max_sum:
#                     max_sum = cur_sum
            
#             return max_sum

#         def kadane(nums):
#             cur_sum = max_sum = nums[0]
#             neg_idx = []
#             for i in range(1, len(nums)):
#                 if nums[i] < 0:
#                     neg_idx.append(i)
#                 if cur_sum <= 0:
#                     cur_sum = nums[i]
#                 else:
#                     cur_sum += nums[i]

#                 if cur_sum > max_sum:
#                     max_sum = cur_sum
#             return max_sum, neg_idx
        
#         case1, neg_idx = kadane(nums)
#         max_val = case1
#         for idx in neg_idx:
#             val = kadane_circle(nums, idx)
#             if val > max_val:
#                 max_val = val

#         return max_val
    
    
# sol2 = Solution().brute_force
# sol = Solution().maxSubarraySumCircular
# print(sol(nums = [-3, -5, 5, 7, -3, -8, 9, 8]))
# # print(sol(nums = [9,0,9,-9,9,-7,3,-2]))
# # print(sol(nums = [0,5,8,-9,9,-7,3,-2]))
# # print(sol(nums = [5,5,0,-5,3,-3,2]))
# # print(sol(nums = [5,5,0,5,6,2]))
# # print(sol(nums = [2,-2,2,7,8,0]))
# # print(sol(nums = [5,-3,5]))
# # print(sol(nums = [5,-3,5]))
# # print(sol(nums = [1,-2,3,-2]))
# # print(sol(nums = [-3,-2,-3]))
# print(sol(nums = [2,3,-1,5,-10,3,5,9]))


# from random import randrange as rd
# def test(func1, func2):
#     n = rd(5, 10)
#     nums = [rd(-10, 10) for i in range(n)]
#     res1 = func1(nums)
#     res2 = func2(nums)
#     if res1 != res2:
#         print(nums)
#         print(res1)
#         print(res2)
#         return True

# # for i in range(100):
# #     # if i % 20 == 0:
# #     #     print(f"iteration {i}")
# #     if test(sol, sol2): break