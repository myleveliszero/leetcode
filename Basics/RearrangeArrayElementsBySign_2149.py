# Status: Good

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        negative = []
        positive = []
        for i in nums:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)
        idxpos = 0
        idxneg = 0
        for i in range(len(nums)): 
            if i % 2 == 0:
                nums[i] = positive[idxpos]
                idxpos += 1
            else:
                nums[i] = negative[idxneg]
                idxneg += 1

        return nums

    
solve = Solution()
print(solve.rearrangeArray(nums = [1,-1]))
