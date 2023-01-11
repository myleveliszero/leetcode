# Status Good

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([stones.count(jewel) for jewel in jewels])
    def version2(self, jewels, stones):
        answ = 0
        for i in jewels:
            for j in stones:
                if i == j: answ += 1
        return answ
    def version3(self, jewels, stones):
        setJ = set(jewels)
        return sum(s in setJ for s in stones)
    
    def version4(self, jewels, stones):
        return sum(map(stones.count, jewels))

solve = Solution()
print(solve.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(solve.numJewelsInStones(jewels = "ab", stones = "aAAbbbb"))
print(solve.version2(jewels = "ab", stones = "aAAbbbb"))
print(solve.version3(jewels = "ab", stones = "aAAbbbb"))
print(solve.version4(jewels = "ab", stones = "aAAbbbb"))
