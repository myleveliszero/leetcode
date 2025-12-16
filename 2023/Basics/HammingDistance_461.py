# Status: Not Bad


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        str1 = bin(x)[2:].zfill(32)
        str2 = bin(y)[2:].zfill(32)
        cnt = 0
        for i,j in zip(str1,str2):
            if i != j:
                cnt += 1
        return cnt
    
solve = Solution()
print(solve.hammingDistance(x = 1, y = 4))

print(solve.hammingDistance(x = 3, y = 1))