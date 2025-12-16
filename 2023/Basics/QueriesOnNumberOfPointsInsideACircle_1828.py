# Status: Not Bad

class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        qlen = len(queries)
        answ = [0]*qlen
        for p in points:
            for q in range(qlen):
                if ((p[0]-queries[q][0])**2 + (p[1]-queries[q][1])**2)**0.5 <= queries[q][2]:
                    answ[q] += 1
        return answ

solve = Solution()
print(solve.countPoints(points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]))