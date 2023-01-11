# Status: Good(99/100)

class Solution:
    def minPartitions(self, n: str) -> int:
        mxstr = '0'
        for i in n:
            if mxstr < i:
                mxstr = i
                if mxstr  == '9': break
        return int(mxstr)
    
    def version2(self, n: str) -> int:
        for i in "987654321":
            if i in n:
                return int(i)
            

solve = Solution()
print(solve.minPartitions("56"))
print(solve.minPartitions("82734"))
print(solve.version2("342545623492349"))
