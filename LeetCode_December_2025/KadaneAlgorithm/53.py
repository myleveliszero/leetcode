from typing import List 
class Solution:
    def brute_force(self, nums):
        max_sum = nums[0]
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                if cur_sum > max_sum:
                    max_sum = cur_sum

        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum
    



sol1 = Solution().brute_force
sol2 = Solution().maxSubArray
# sol3 = Solution().maxSubArray_2

# print(sol3([-1, 10, -1, 3, 6, 5, -4]))
print(sol1([-1, 10, -1, 3, 6, 5, -4]))
print(sol1([-2,1,-3,4,-1,2,1,-5,4]))
print(sol1([5,4,-1,7,8]))
# print(sol2([4,-1,2,-7,3,4]))
print(sol2([-2,1,-3,4,-1,2,1,-5,4]))
print(sol2([5,4,-1,7,8]))

from random import randrange as rd
def test(func1, func2):
    n = rd(1, 10)
    nums = [rd(-10, 11) for i in range(n)]
    res1 = func1(nums)
    res2 = func2(nums)
    if res1 != res2:
        print("Wrong")
        print(nums)
        return True

# for i in range(100):
#     # if i % 20 == 0:
#     #     print(f"iteration {i}")
#     if test(sol3, sol2): break