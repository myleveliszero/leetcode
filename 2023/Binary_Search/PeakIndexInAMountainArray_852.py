# Status: Good

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right= 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] > arr[mid+1]:
                if arr[mid] > arr[mid-1]:
                    return mid
                else:
                    right = mid-1
            elif arr[mid] < arr[mid+1]:
                left = mid+1
    def version2(self, arr):
        left, right= 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid-1
        

solve = Solution()
print(solve.peakIndexInMountainArray(arr = [9,10,6,5,4,3,2,1,0]), end=" --> ")
print(solve.peakIndexInMountainArray(arr = [0,1,2,6,7,8,9,11,12,3]), end=" --> ")
print(solve.peakIndexInMountainArray(arr = [0,10,12,13,14,9,8,7,6,5]), end=" --> ")
print(solve.peakIndexInMountainArray(arr = [0,1,2,6,7,8,9,11,12,3]), end=" --> ")
print(solve.peakIndexInMountainArray(arr = [0,2,1,0]), end=" --> ")
print(solve.peakIndexInMountainArray(arr = [0,1,0]), end=" --> ")
print(solve.peakIndexInMountainArray(arr = [0,10,5,2]))
