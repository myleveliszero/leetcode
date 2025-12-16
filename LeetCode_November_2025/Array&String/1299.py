from typing import *
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curIdx, maxIdx = 0, 0
        while curIdx < len(arr)-1:
            maxVal = 0
            for j in range(curIdx+1, len(arr)):
                if arr[j] >= maxVal:
                    maxVal = arr[j]
                    maxIdx = j

            while curIdx < maxIdx:
                arr[curIdx] = arr[maxIdx]
                curIdx += 1

        arr[-1] = -1
        return arr
    
     
sol = Solution().replaceElements
# print(sol([17,18,5,4,6,1]))
print(sol([17,18,5,4,6,6,6,6,6,7]))