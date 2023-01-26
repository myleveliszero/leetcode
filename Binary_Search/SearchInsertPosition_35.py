# Status: Good

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if mid == left:
            return mid
        else:
            return mid + 1

            
    def version2(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left
        

solve = Solution()
print(solve.searchInsert(nums = [1,3,5,6], target = 5), end=" --> ")
print(solve.searchInsert(nums = [1,3,5,6], target = 2), end=" --> ")
print(solve.searchInsert(nums = [1,3,5], target = 4), end=" --> ")
print(solve.searchInsert(nums = [1,3], target = 2), end=" --> ")
print(solve.searchInsert(nums = [1,3,5,6], target = 7), end=" --> ")
print(solve.searchInsert(nums = [1,3,5,6], target = 0), end=" --> ")
print(solve.searchInsert(nums = [-3,-2,-1,1,3,5,6], target = 0), end=" --> ")
print(solve.searchInsert(nums = [-3,-2,-1,1,3,5,6], target = -4), end=" --> ")
print(solve.searchInsert(nums = [-3,-2,-1,1,3,5,6], target = 7))

print(solve.version2(nums = [1,3,5,6], target = 5), end=" --> ")
print(solve.version2(nums = [1,3,5,6], target = 2), end=" --> ")
print(solve.version2(nums = [1,3,5], target = 4), end=" --> ")
print(solve.version2(nums = [1,3], target = 2), end=" --> ")
print(solve.version2(nums = [1,3,5,6], target = 7), end=" --> ")
print(solve.version2(nums = [1,3,5,6], target = 0), end=" --> ")
print(solve.version2(nums = [-3,-2,-1,1,3,5,6], target = 0), end=" --> ")
print(solve.version2(nums = [-3,-2,-1,1,3,5,6], target = -4), end=" --> ")
print(solve.version2(nums = [-3,-2,-1,1,3,5,6], target = 7))