# Status: Good

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        answ = 0
        for i in range(len(points)-1):
            x1,y1 = points[i][0], points[i][1]
            x2,y2 = points[i+1][0], points[i+1][1]
            distanceX1 = abs(x2 - x1) 
            distanceY1 = abs(y2 - y1)
            if distanceX1 > distanceY1:
                answ += distanceX1
            else:
                answ += distanceY1
        return answ

solve = Solution()
print(solve.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]))
print(solve.minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))