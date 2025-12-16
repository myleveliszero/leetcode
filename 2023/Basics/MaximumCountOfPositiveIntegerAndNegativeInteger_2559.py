# Status: Not Bad

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos, neg = [], []
        for i in nums:
            if i > 0:
                pos.append(i)
            elif i < 0:
                neg.append(i)
        return max(len(pos), len(neg)) 

solve = Solution()
print(solve.maximumCount([-2,-1,-1,1,2,3]))
print(solve.maximumCount([-3,-2,-1,0,0,1,2]))
print(solve.maximumCount([5,20,66,1314]))
    

