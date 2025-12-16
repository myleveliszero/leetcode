from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            return count 

        ans = [hammingWeight(i) for i in range(n+1)]
        return ans


sol = Solution().countBits
print(sol(5))