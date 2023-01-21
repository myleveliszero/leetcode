# Status: Good

class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        rows = [0 for i in range(m)]
        cols = [0 for j in range(n)]
        for idx in indices:
            rows[idx[0]] += 1
            cols[idx[1]] += 1
        answ = 0 
        for i in rows:
            for j in cols:
                if (i + j) % 2 != 0:
                    answ += 1
        return answ


solve = Solution()
print(solve.oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))
