# Status: Not Bad

class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        """
        onesRowi, onesColj, zerosRowi, zerosColj
        diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
        return diff
        """
        ilen, jlen = len(grid), len(grid[0])
        onesRowi, onesColj = [0]*ilen, [0]*jlen
        zerosRowi, zerosColj = [0]*ilen, [0]*jlen
        for i in range(ilen):
            for j in range(jlen):
                if grid[i][j] == 1:
                    onesRowi[i] += 1
                    onesColj[j] += 1
                else:
                    zerosRowi[i] += 1
                    zerosColj[j] += 1
        for i in range(ilen):
            for j in range(jlen):
                grid[i][j] = onesRowi[i]+onesColj[j]-zerosRowi[i]-zerosColj[j]
        
        return grid



solve = Solution()
print(solve.onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]]))
