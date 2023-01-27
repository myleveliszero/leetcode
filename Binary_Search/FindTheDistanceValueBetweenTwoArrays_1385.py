# Status: Good

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        a2len = len(arr2)
        def check(i, val, j):
            left, right = 0, a2len-1
            while left<=right:
                mid = left + (right-left)//2
                # if not(arr2[mid] < i or arr2[mid] > j):
                if arr2[mid] >= i and arr2[mid] <= j:
                    return 0
                elif arr2[mid] < val:
                    left = mid+1
                else:
                    right = mid-1
            return 1

        return sum(check(val-d,val,val+d) for val in arr1)


    def simple(self, arr1, arr2, d):
        ans = 0
        for i in arr1:
            condition = True
            for j in arr2:
                if abs(i-j) <= d:
                    condition = False
                    break
            if condition:
                ans += 1
        return ans

solve = Solution()
print(solve.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2), end = " --> ")
print(solve.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3), end = " --> ")
print(solve.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))

print(solve.simple(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2), end = " --> ") # ans = 2
print(solve.simple(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3), end = " --> ") # ans = 2
print(solve.simple(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6)) # ans = 1