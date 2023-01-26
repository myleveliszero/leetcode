# Status: Not Bad

class Solution:
    def search(self, nums, target):
        left, right = 0 , len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[left] < nums[mid]:
                if target > nums[left] and target < nums[mid]:
                    right = mid-1
                elif target < nums[left] or target > nums[mid]:
                    left = mid+1
            else:
                if target < nums[right] and target > nums[mid]:
                    left = mid+1
                elif target > nums[right] or target < nums[mid]:
                    right = mid-1
        return -1

solve = Solution()
print(solve.search(nums = [5,1,2,3,4], target = 1), end=' --> ')
print(solve.search(nums = [4,6,-3,-2,-1,1, 2, 3], target = 3), end=' --> ')
print(solve.search(nums = [4,5,6,7,8,1,2,3], target = 8), end=' --> ')
print(solve.search(nums = [3,1], target = 0), end=' --> ')
print(solve.search(nums = [3,1], target = 3), end=' --> ')
print(solve.search(nums = [3,5, 1], target = 5), end=' --> ')
print(solve.search(nums = [-6,1], target = -1), end=' --> ')
print(solve.search(nums = [6,1], target = 1), end=' --> ')
print(solve.search(nums = [4,5,6,7,0,1,2], target = 6), end=' --> ')
print(solve.search(nums = [1], target = 1), end=' --> ')
print(solve.search(nums = [4,5,6,7,0,1,2], target = 2), end=' --> ')
print(solve.search(nums = [4,5,6,-3,-2,-1,0,1,2], target = -1))
