from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            y = height[left] if height[left] < height[right] else height[right]
            x = right-left
            area = x * y
            max_area = max_area if max_area > area else area
            # area = min(height[left], height[right]) * (right-left)
            # max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
sol = Solution().maxArea

from random import randrange as r

def test(func1):
    n = r(10**3, 3*10**3)
    nums = [r(0, 100) for _ in range(n)]
    res = func1(nums)
    print(nums)

for i in range(3):
    test(sol)