# Status: Good

import collections

class Solution:
    def countPairs(self, nums:  list[int], k: int) -> int:
        """
        return number of pairs such that:
        nums[i] == nums[j] and (i * j) is divisible by k
        0 <= i < j < n
        """
        # Naive approach 
        answ, nlen = 0, len(nums)
        for i in range(nlen):
            for j in range(i+1, nlen):
                if nums[i] == nums[j] and i*j % k == 0:
                    answ += 1
        return answ
    def version2(self, nums, k):
        answ , sameval = 0, collections.defaultdict(list)
        for idx, val in enumerate(nums):
            sameval[val].append(idx)
        for listidx in sameval.values():
            for i in range(len(listidx)):
                for j in range(i+1, len(listidx)):
                    if listidx[i]*listidx[j] % k == 0:
                        answ += 1
        return answ

solve = Solution()
print(solve.countPairs(nums = [3,1,2,2,2,1,3], k = 2))
print(solve.version2(nums = [3,1,2,2,2,1,3], k = 2))