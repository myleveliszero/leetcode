from typing import *
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        def twoPointers(num):
            print(num)
            left, right = 0, 1
            while right < len(num):
                if 2*num[left] == num[right]:
                    return True
                elif num[right]//num[left] + 1 > 2:
                    left += 1
                else: 
                    right += 1
            return False
        zeroCnt = 0
        for elem in arr:
            if elem == 0:
                zeroCnt += 1
            if zeroCnt == 2:
                return True
        arr.sort()
        nums1, nums2 = [], []
        for elem in arr:
            if elem > 0:
                nums1.append(elem)
            elif elem < 0:
                nums2.append(elem*(-1))
        nums2.reverse()
        return twoPointers(nums1) or twoPointers(nums2)


sol = Solution().checkIfExist
# print(sol(arr = [10,2,5,3]))
# print(sol([-20,8,-6,-14,0,-19,14,-6]))
print(sol([-10,12,-20,-8,15]))
print(sol(arr = [0,2,-2]))
print(sol(arr = [0,0]))
