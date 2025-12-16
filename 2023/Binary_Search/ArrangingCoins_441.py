# Status: Good

import math

class Solution:
    def arrangeCoins(self, N: int) -> int:
        if N == 1: return 1
        if N == 3: return 2

        low, high = 2, N//2
        while low <= high:
            mid = low + (high-low)//2
            staircase = mid*(mid+1)//2
            if staircase == N:
                return mid
            elif N > staircase:
                low = mid + 1
            else:
                high = mid-1
        return high

    def mathmethod(self, n):
        return math.floor((-0.5 + (2*n+0.25)**0.5))

    def simple(self, n):
        i = 0
        while n >= 0:
            i += 1
            n -= i

        return i if n == 0 else i-1

solve = Solution()
print("\nBinary Search\n")
print(f"output: {solve.arrangeCoins(5)}", f"expected: 2")
print(f"output: {solve.arrangeCoins(8)}", f"expected: 3")
print(f"output: {solve.arrangeCoins(1073741824)}", f"expected: 46340")
print(f"output: {solve.arrangeCoins(2147483647)}", f"expected: 65535")

print("\nMath Method\n")
print(f"output: {solve.mathmethod(5)}", f"expected: 2")
print(f"output: {solve.mathmethod(8)}", f"expected: 3")
print(f"output: {solve.mathmethod(1073741824)}", f"expected: 46340")
print(f"output: {solve.mathmethod(2147483647)}", f"expected: 65535")

print("\nIterative Method\n")
print(f"output: {solve.simple(5)}", f"expected: 2")
print(f"output: {solve.simple(8)}", f"expected: 3")
print(f"output: {solve.simple(1073741824)}", f"expected: 46340")
print(f"output: {solve.simple(2147483647)}", f"expected: 65535")