# Status Not Bad

class Solution:
    def minimumSum(self, num: int) -> int:
        answ = sorted(str(num))
        return int(answ[0]+answ[3])+int(answ[1]+answ[2])    

solve = Solution()
print(solve.minimumSum(1234))
print(solve.minimumSum(2345))