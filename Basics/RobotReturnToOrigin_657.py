# Status: Good

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l,d = 0,0
        for i in moves:
            if i == 'L':
                l+=1
            elif i == 'R':
                l-=1
            elif i == 'U':
                d-=1
            else:
                d+=1
        return True if l==0 and d==0 else False
    
solve = Solution()
print(solve.judgeCircle("LLLLRRRRUDUDDUR"))  
print(solve.judgeCircle("UD"))
print(solve.judgeCircle("LLLLRRRUDUDDUR"))  
print(solve.judgeCircle("U"))