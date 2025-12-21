from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = dict()
        for i in range(len(nums)):
            if nums[i] in hmap and i - hmap[nums[i]] <= k:
                return True   
            hmap[nums[i]] = i                 
        return False           

    def containsNearbyDuplicate_2(self, nums: List[int], k: int) -> bool:
        hset = set()
        for i in range(len(nums)):
            if nums[i] in hset:
                return True
            hset.add(nums[i])
            if len(hset) > k:
                hset.remove(nums[i-k])
        return False
    
print(Solution().containsNearbyDuplicate_2([1,4,2,3,1,2], 3))