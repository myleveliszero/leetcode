# from typing import List
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         prefix = [nums[0]]
#         for i in range(1, len(nums)):
#             prefix.append(prefix[-1] + nums[i])

#         count = 0
#         j = 0
#         for i in range(len(nums)):
#             j = j if j >= i else i
#             left_sum = prefix[i-1] if i > 0 else 0
#             # sub_sum = prefix[j] - left_sum
#             # while sub_sum < k and j < len(nums)-1:
#             #     j += 1
#             #     sub_sum = prefix[j] - left_sum
        
#             # if sub_sum == k:
#             #     count += 1
        
#         return count
    
# sol = Solution().subarraySum
# print(sol([-7, 2, 2, -6, -4, -7, -3, -3, -7], k = -2))
# print(sol([-7, -4, 4, 4, -10, -10], k = 0))
# print(sol([-8, -5, 5, 5, -10, -4, 1, -5], k = 7))


# from random import randrange as r 

# def test(func1):
#     n = r(5, 10)
#     nums = [r(-10, 10) for i in range(n)]
#     k = r(-10, 10)

#     func1(nums, k)
#     print("start")
#     print(nums)
#     print(k)
#     # print("end")

# for i in range(10):
#     test(sol)


# # [1, 9, 0, -2, -10, -5, 3, -10, -5, 7, -8, 0, -8, -10, -4, 8, 3, 7, -8, 9, -8, 3, -3, -10, 0, 3, -7, 5, -6, 3, -6, 5, -2, 1, -2, -7, 4, -10, 6, -7, 7, -5, -4, -1, 1, 4, -7, -6, -2, -5, -1, -1, 2, 4, 3, 7, 6, -2, -2, -8, -2, 9, -3, -5, -6, -7, -9, 6, 0, -2, -7, 2, 0, -10, 5, -7, 2, 3, -9, 6, 1, -2, -8, -10, -9, 5, 5, 8, -7, 6, 6, 4, 6, 2, -7, 4, -10, -6, -2, -9, 6, -3, 1, 2, 3, 2, 6, 2, -3, -5, -10, 3, 2, 9, -1, -1, -2, -6, -10, -2, 7, 4, 9, -2, -2, 8, -1, 1, 0, 7, 8, 5, 4, -3, 6, 6, 7, -3, 0, -8, 0, 9, -9, 6, -6, -10, -9, 6, -1, 0, 5, -5, -6, -6, -1, -6, 4, 4, -3, 3, -10, 1, -4, -10, 4, 4, -8, -7, -3, 9, -6, 2, -3, 3, 8, -4, -4, -1, 0, -3, -1, -10, 2, -8, 5, -7]