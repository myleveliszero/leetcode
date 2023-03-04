# Status: Good

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l,r,u,d = 0,0,0,0
        for i in moves:
            if i == 'L':
                l+=1
            elif i == 'R':
                r+=1
            elif i == 'U':
                u+=1
            else:
                d+=1
        return True if l==r and u==d else False

solve = Solution()
print(solve.judgeCircle("LLLLRRRRUDUDDUR"))  
print(solve.judgeCircle("UD"))
print(solve.judgeCircle("LLLLRRRUDUDDUR"))  
print(solve.judgeCircle("U"))