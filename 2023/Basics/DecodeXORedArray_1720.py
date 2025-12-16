# Status: Good

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        answ = [first]
        for i in range(len(encoded)):
            answ.append(answ[i]^encoded[i])
        return answ

solve = Solution()
print(solve.decode(encoded = [1,2,3], first = 1))
print(solve.decode(encoded = [6,2,7,3], first = 4))
