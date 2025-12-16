from typing import*
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, left, right):
            right -= 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left+1, right-1

        n = len(nums)
        k %= n
        reverse(nums, 0, n)
        reverse(nums, 0, k)
        reverse(nums, k, n)

        # return nums




sol = Solution().rotate
print(sol([-53, 35, 10, 62, -44, -79, 38, 68], k=6))    
print(sol([-53, 35, 10, 62, -44, -79, 38, 68], k=25350))    
# print(sol([29, -12], k=1))    
# print(sol([-1,-100,3,99], k=3))    
# print(sol([-1,-100,3,99,55,66], k=6))    
# print(sol([-1,-100,3,99,55,66], k=2))    
# print(sol([-1,-100,3,99,55,66], k=3))    
# print(sol([-1,-100,3,99,55,66], k=4))    
# print(sol([-1,-100,3,99,55,66], k=0))    
print(sol([-1,-100,3,99,55,66,77,88], k=4))    
print(sol([1,2,3,4,5,6,7], k=2))

def rotate(nums: List[int], k: int):
    if len(nums) == 1:
        return nums
    for i in range(k):
        nums.insert(0, nums.pop())
    return nums

from random import randrange
from typing import *

def test(func1, func2, size, a, b):
    nums = [randrange(a, b) for _ in range(size)]
    nums1, nums2 = nums.copy(), nums.copy()
    k = randrange(0, 100000)
    res1 = func1(nums1, k)
    res2 = func2(nums2, k)
    if res1 != res2:
        print(nums)
        print(res1)
        print(res2)
        print("k: ", k)
        return True
    return False

for i in range(1000):
    size = randrange(1, 20)
    print("iter: ", i, "; size: ", size)
    if test(sol, rotate, size, -2147483648, 2147483647):
        break

#-2147483648
#2147483647