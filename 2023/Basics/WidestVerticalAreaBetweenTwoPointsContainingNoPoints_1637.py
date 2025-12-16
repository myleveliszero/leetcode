# Status: Not Bad

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        coordinatsX = [i[0] for i in points]
        coordinatsX.sort()
        answmax = 0
        for i in range(1, len(coordinatsX)):
            distance = coordinatsX[i]-coordinatsX[i-1]
            if distance > answmax:
                answmax = distance
        return answmax

solve = Solution()
print(solve.maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))
print(solve.maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
print(solve.maxWidthOfVerticalArea([[1,5],[1,70],[3,1000],[55,700],[999876789,53],[987853567,12]]))