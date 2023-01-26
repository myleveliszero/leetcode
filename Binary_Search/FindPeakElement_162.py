# Status: Good

class Solution:
    def findPeakElement1(self, nums: list[int]) -> int:
        left, right= 0, len(nums)-1
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return right

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
    def findPeakElement(self, nums):
        if len(nums) == 1: return 0
        left, right= 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:                
                right = mid
            else:
                left = mid + 1
        return left
        

solve = Solution()
print(solve.findPeakElement(nums = [6,2, 3,7]),end=" --> ")
print(solve.findPeakElement(nums = [6,5,4,3,2,3,2]),end=" --> ")
print(solve.findPeakElement(nums = [1,2,3,4,5,8,7,1]),end=" --> ")
print(solve.findPeakElement(nums = [3,1,2]),end=" --> ")
print(solve.findPeakElement(nums = [15]))