from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        if len(arr) == 2 and arr[0] == arr[1]: return 1
        if len(arr) == 2 and arr[0] != arr[1]: return 2

        cur_len = 0
        max_len = 1 
        add_1 = False
        for k in range(1, len(arr)-1):
            if arr[k-1] != arr[k] or arr[k] != arr[k+1]:
                add_1 = True
            if  arr[k-1] > arr[k] < arr[k+1] or \
                arr[k-1] < arr[k] > arr[k+1]:
                cur_len += 1
                if (cur_len+2 > max_len):
                    max_len = cur_len+2
            else:
                cur_len = 0
            
            if cur_len > max_len:
                max_len = cur_len
        
        if max_len == 1 and add_1: return 2

        return max_len

sol = Solution().maxTurbulenceSize
print(sol(arr = [9,4,2,10,7,8,8,1,9]))
print(sol(arr = [4,8,12,16]))
print(sol(arr = [100]))
print(sol(arr = [100,150,100]))

from random import randrange as rd

def test(func1):
    n = rd(1000, 5000)
    nums = [rd(0,10) for i in range(n)]
    res = func1(nums)
    print(nums)
    print("------------------------")
    print(res)

# for i in range(5):
#     test(sol)
    
