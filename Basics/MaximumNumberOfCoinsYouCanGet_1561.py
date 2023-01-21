# Status: Good

class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        answ, plen = 0, len(piles)
        startidx = plen // 3
        for i in range(startidx):
            answ += piles[startidx+2*i]
        return answ
    def version2(self, piles):
        return sum(sorted(piles)[len(piles)//3 :: 2])

solve = Solution()
print(solve.maxCoins(piles = [2,4,1,2,7,8]))
print(solve.maxCoins(piles = [9,8,7,6,5,1,2,3,4]))
print(solve.version2(piles = [9,8,7,6,5,1,2,3,4]))
