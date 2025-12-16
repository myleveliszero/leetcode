# Status: Bad

class Solution:
    # pref[i] = arr[0]^arr[1]^...^arr[i]
    # Find arr
    def findArray(self, pref: list[int]) -> list[int]:
        answ = [0]*len(pref)
        answ[0] = pref[0]
        previ = answ[0]
        for i in range(1,len(pref)):
            answ[i] = previ^pref[i]
            previ = previ^answ[i]
        return answ
        
solve = Solution()
print(solve.findArray([5,2,0,3,1]))