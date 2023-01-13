# Status: Good

class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        left, right = int(s[1]), int(s[-1])
        cur = s[0]
        last = chr(ord(s[-2])+1)
        answ = []
        while cur != last:
            for i in range(left, right+1):
                answ.append(cur+str(i))
            cur = chr(ord(cur)+1)
        return answ
    def same(self, s: str):
        answ = []
        for i in range(ord(s[0]), ord(s[-2])+1):
            for j in range(int(s[1]), int(s[-1])+1):
                answ.append(chr(i)+str(j))
        return answ

solve = Solution()
print(solve.cellsInRange(s = "K1:L2"))
print(solve.cellsInRange(s = "A1:F1"))
print(solve.same(s = "K1:L2"))