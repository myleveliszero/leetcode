# Status: Not Bad

class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n,'b')
        for i in range(32-len(n)):
            n = '0' + n
        n = n[::-1]
        return int(n, 2)

solve = Solution()
print(solve.reverseBits(43261596))