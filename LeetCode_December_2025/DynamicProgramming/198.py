from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def bt(nums, visit, memo, idx, cur_sum, max_val):            
            if cur_sum > max_val[0]:
                max_val[0] = cur_sum
            if idx >= len(nums):
                return 
            if visit and abs(idx-visit[-1]) <= 1:
                bt(nums, visit, memo, idx+1, cur_sum, max_val)
                return 
            if idx in memo:
                cur_sum += memo[idx]
                if cur_sum > max_val[0]:
                    max_val[0] = cur_sum
                return 

            bt(nums, visit, memo, idx+1, cur_sum, max_val)
            visit.append(idx)
            cur_sum += nums[idx]
            bt(nums, visit, memo, idx+1, cur_sum, max_val)
            memo[idx] = max_val[0]
            visit.pop()
            return

        max_val = [0]
        memo = {}
        bt(nums, [], memo, 0, 0, max_val)

        return max_val.pop()
    
sol = Solution().rob
print(sol(nums = [1,2,3,1]) == 4)
print(sol(nums = [2,7,9,3,1]) == 12)
print(sol(nums = [2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1]) == 56)
print(sol(nums = [99,99,99,99,99,99,99,99,99]) == 495)
print(sol(nums = [347, 359, 155, 226, 384, 327, 30, 277, 175, 290, 97, 31, 298, 33, 36, 7,
                348, 16, 219, 62, 175, 108, 269, 120, 204, 226, 191, 269, 74, 54, 82, 309,
                278, 16, 338, 187, 303, 114, 98, 23, 193, 376, 399, 309, 125, 211, 26, 148,
                162, 329, 103, 325, 379, 283, 116, 296, 127, 99, 202, 162, 345, 260, 315, 48, 
                50, 219, 33, 262, 196, 251, 352, 140, 25, 288, 265, 2, 261, 16, 392, 325, 63, 
                388, 67, 203, 112, 146, 280, 48, 273, 72, 175]) == 10692)

# import random

# def test(func1):
#     length = random.randrange(1, 100)
#     nums = [random.randrange(0, 400) for _ in range(length)]
#     res = func1(nums)
#     print(nums)
#     return res

# for i in range(10):
#     print("\n\n---------------------")
#     print("max_rob:  ", test(sol))

