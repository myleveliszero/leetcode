from typing import*
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            twosum = numbers[left]+numbers[right]
            if twosum == target:
                return [left+1, right+1]
            elif twosum > target:
                right -= 1
            else:
                left += 1

sol = Solution().twoSum
print(sol(numbers = [2,7,11,15], target = 9))
print(sol(numbers = [2,3,4], target = 6))
print(sol(numbers = [-1,0], target = -1))