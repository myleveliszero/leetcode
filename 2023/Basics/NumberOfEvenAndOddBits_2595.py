# Status: Good

class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        s = format(int(n), 'b')
        s = s[::-1]
        even, odd = 0, 0 
        for i in range(len(s)):
            if s[i] == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]

solve = Solution()
print(solve.evenOddBit(n = 17))
print(solve.evenOddBit(n = 1000))