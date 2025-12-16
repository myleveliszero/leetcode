# Status Good

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(i) for i in accounts)
    def version2(self, accounts):
        return max(map(sum, accounts))

solve = Solution()
print(solve.maximumWealth([[1,5],[7,3],[3,5]]))
print(solve.version2([[1,5],[7,3],[3,5]]))   