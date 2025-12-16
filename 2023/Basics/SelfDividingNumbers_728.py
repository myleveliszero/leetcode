# Status: Good

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        answ = []
        for n in range(left, right+1):
            selfdivide = True
            for digit in str(n):
                if digit == '0':
                    selfdivide = False
                    break
                if n % int(digit) != 0:
                    selfdivide = False
                    break
            if selfdivide:
                answ.append(n)
        return answ
    def version2(self, left, right):
        answ = []
        for i in range(left, right+1):
            if  i > 9:
                icopy, selfdivide = i, True
                while i:
                    digit = i % 10
                    if digit == 0: 
                        selfdivide = False
                        break
                    if icopy % digit != 0:
                        selfdivide = False
                        break
                    i //= 10
                if selfdivide:
                    answ.append(icopy) 
            else:
               answ.append(i)
        return answ





solve = Solution()
print(solve.selfDividingNumbers(left = 1, right = 22))
print(solve.selfDividingNumbers(left = 47, right = 85))
print(solve.version2(left = 1, right = 22))
print(solve.version2(left = 47, right = 85))