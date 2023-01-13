# Status: Good

class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        idxM,idxG,idxP = 0, 0, 0
        val = 0
        for i in range(len(garbage)):
            val += len(garbage[i])
            if 'M' in garbage[i]:
                idxM = i
            if 'G' in garbage[i]:
                idxG = i
            if 'P' in garbage[i]:
                idxP = i
        return sum(travel[:idxM]+travel[:idxG]+travel[:idxP]) + val

solve = Solution()
print(solve.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]))
print(solve.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))
