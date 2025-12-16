class Solution:
    def addBinary(self, a: str, b: str) -> str:        
        return bin(int(a,2)+int(b,2))
 
sol = Solution().addBinary
print(sol('5','6'))