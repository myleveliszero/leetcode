from typing import*
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = set()
        for i in range(len(nums)):
            if i > k:
                hset.remove(nums[i-k-1])
            if nums[i] in hset:
                return True
            hset.add(nums[i])
        return False
    
sol = Solution().containsNearbyDuplicate
print(sol([1,2,1], k = 0))
print(sol([1,4,2,3,1,2], k = 3))
print(sol(nums = [1,0,1,1], k = 1))
print(sol(nums = [1,2,3,1,2,3], k = 2))
print(sol([1,2,3,1,9,1], k = 2))
