from typing import*
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minsum = float('inf')
        h1, h2 = dict(), dict()
        for idx, val in enumerate(list1):
            if val not in h1:
                h1[val]=idx
        for idx, val in enumerate(list2):
            if val not in h2:
                h2[val]=idx
        
        for key in h1.keys():
            if key in h2:
                cursum = h1[key]+h2[key]
                if cursum < minsum:
                    minsum = cursum
                h1[key] = cursum
            else:
                h1[key] = 9999
        
        res = []
        for key in h1.keys():
            if h1[key] == minsum:
                res.append(key)
        
        return res
    

