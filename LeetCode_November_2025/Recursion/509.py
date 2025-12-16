class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return 1 if n else 0
        prev, cur = 1, 1
        for i in range(2, n):
            cur, prev = cur+prev, cur
        return cur