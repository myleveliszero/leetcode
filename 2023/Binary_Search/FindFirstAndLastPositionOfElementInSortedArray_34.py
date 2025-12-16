# Status: Good

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bs(arr, tar):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] < tar:
                    left = mid+1
                else:
                    right = mid-1
            return left
        
        l, r = bs(nums,target-0.9), bs(nums, target+0.9)
        
        if l == r:  return [-1,-1]
        else:   return [l, r-1]
            
    def version2(self, nums ,target):
        ans = [-1, -1]
        if nums == []: return ans

        idx = -1
        l, r = 0, len(nums)-1
        while l <= r:
            m = l+(r-l)//2
            if target == nums[m]:
                r = m-1
                idx = m
            elif target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
        if nums[idx] != target:
            return ans
        else:
            ans[0] = idx
        
        idx = -1
        r = len(nums)-1
        while l <= r:
            m = l+(r-l)//2
            if target == nums[m]:
                l = m+1
                idx = m
            elif target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
        ans[1] = idx
        return ans


solve = Solution()
print(solve.searchRange(nums=[5,7,7,8,8,8,8,8,8,8,8,9,9,9,10], target=8))
print(solve.searchRange(nums=[-5,1,1,1,1,1,1,1,1,1,1,5], target=5))
print(solve.searchRange(nums=[], target=5))

print(solve.version2(nums=[2,2], target=3))
print(solve.version2(nums=[5,7,7,8,8,8,8,8,8,8,8,9,9,9,10], target=8))
print(solve.version2(nums=[-5,1,1,1,1,1,1,1,1,1,1,5], target=5))
print(solve.version2(nums=[], target=5))