# Status: Not Bad

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        for i in num:
            if i == '9':
                continue
            else:
                change = i
                break
        nmax, nmin = "", ""
        for i,j in zip(num, num):
            if i == change:
                nmax += '9'
            else:   
                nmax += i
            
            if j == num[0]:
                nmin += '0'
            else:
                nmin += j
        
        return int(nmax) - int(nmin)
    
solve = Solution()
print(solve.minMaxDifference(90))