# Status Good

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and i == nums[i] else i

    def lastattempt(self, nums):
        nums.sort(reverse=True)
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] > mid:
                low = mid+1
            else:
                high = mid-1
        return -1 if low < len(nums) and low == nums[low] else low



    def firstattempt(self, nums):
        nums.sort()
        for i in range(1, nums[-1]+1):
            low, high = 0, len(nums)-1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] < i:
                    low = mid+1
                else:
                    high = mid-1
            idx = low
            if len(nums)-idx == i:
                return i
        return -1

solve = Solution()
print(solve.specialArray(nums = [3, 6, 7, 7, 0]))
print(solve.specialArray(nums = [0,4,3,0,4]))
print(solve.specialArray(nums = [3,5]))
print(solve.specialArray(nums = [0,0]))
