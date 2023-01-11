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
    def version3(self, n: str) -> int:
        return int(max(n))
            

solve = Solution()
print(solve.minPartitions("6633256"))
print(solve.minPartitions("82734"))
print(solve.version2("342545623492349"))
print(solve.version3("2356238"))
