# Status: Not Bad

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2)+int(b, 2) , 'b')
    
solve = Solution()
print(solve.addBinary(a = "1010", b = "1011"))