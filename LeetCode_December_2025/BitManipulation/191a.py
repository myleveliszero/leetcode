class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
    
sol = Solution().hammingWeight
print(sol(2147483645))
        