class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0]*32
        for i in range(len(bits)):
            if n > 0:
                bits[i] = n & 1
                n = n >> 1
        ans, j = 0, 0
        for i in reversed(range(len(bits))):
            ans += bits[i]*(2**j)
            j += 1 

        return ans
            

sol = Solution().reverseBits
print(sol(43261596))
