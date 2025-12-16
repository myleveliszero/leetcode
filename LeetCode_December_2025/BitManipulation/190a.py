class Solution:
    def reverseBits(self, n: int) -> int:
        ans, i = 0, 31
        while n > 0:
            ans += (n & 1) * (1 << i)
            n = n >> 1
            i -= 1
        return ans

sol = Solution().reverseBits
print(sol(28))