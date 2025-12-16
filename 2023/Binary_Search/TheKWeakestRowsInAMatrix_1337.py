# Status: Bad

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
       pass
    def simple (self, mat, k):
        ranking = []
        for idx, row in enumerate(mat):
            ranking.append((sum(row), idx))
        ranking.sort()
        return [i[1] for i in ranking[:k]]

solve = Solution()
print(solve.kWeakestRows(mat = 
                    [[1,1,0,0,0],
                    [1,1,1,1,0],
                    [1,0,0,0,0],
                    [1,1,0,0,0],
                    [1,1,1,1,1]], 
                        k = 3))

print(solve.kWeakestRows(mat = 
                    [[1,0,0,0],
                    [1,1,1,1],
                    [1,0,0,0],
                    [1,0,0,0]], 
                    k = 2))