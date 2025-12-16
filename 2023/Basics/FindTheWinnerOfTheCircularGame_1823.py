# Status: Bad

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i+1 for i in range(n)]
        while len(circle) != 1:
            for i in range(k-1):
                circle.append(circle.pop(0))
            circle.pop(0)
        return circle[0]

solve = Solution()
print(solve.findTheWinner(n = 5, k = 2))
print(solve.findTheWinner(n = 6, k = 5))