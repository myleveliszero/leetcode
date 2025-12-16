# Status: Bad

class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        blen = len(boxes)
        answ = []
        for i in range(blen):
            curoper = 0
            for j in range(blen):
                if boxes[j] == '1':
                    curoper += abs(i-j)
            answ.append(curoper)
        return answ

solve = Solution()
print(solve.minOperations("110"))
print(solve.minOperations("001011"))