# Status: Good

class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        answ, maxLen = 0, 0
        for r in rectangles:
            rmin = min(r[0],r[1])
            if rmin > maxLen:
                maxLen = rmin
        for r in rectangles:
            if maxLen == r[0]:
                if r[0] - r[1] <= 0:
                    answ += 1 
            elif maxLen == r[1]:
                if r[1] - r[0] <= 0:
                    answ += 1
        return answ
    def version2(self, rectangles):
        answ, mx = 0, 0
        for l, w in rectangles:
            side = min(l, w)
            if side > mx:
                answ, mx = 1, side
            elif side == mx:
                answ += 1
        return answ

solve = Solution()
print(solve.countGoodRectangles(rectangles = [[2,3],[1,2],[3,1],[3,1],[2,3],[2,1],[2,3],[1,3],[3,1],[1,3],[3,2],[2,3],[2,1],[1,3],[3,2],[1,2],[3,1],[2,1],[1,3],[3,2]]))
print(solve.countGoodRectangles(rectangles =  [[2,3],[3,7],[4,3],[3,7]]))
print(solve.version2(rectangles =  [[2,3],[3,7],[4,3],[3,7]]))