# Status: Good

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            
            if nums[slow] != 0:
                slow += 1
        print(nums)

    def firstattempt(self, nums):
        """
        A two-pointer approach could be helpful here.
        The idea would be to have one pointer for iterating 
        the array and another pointer that just works on 
        the non-zero elements of the array.
        """
        iszero, nonzero = 0, 1
        while nonzero < len(nums):
            if nums[iszero] == 0 and nums[nonzero] == 0:
                nonzero += 1
            elif nums[iszero] == 0 and nums[nonzero] != 0:
                nums[iszero], nums[nonzero] = nums[nonzero], nums[iszero]
                iszero += 1
                nonzero += 1
            else: # iszero != 0 and nonzero != 0  || iszero != 0 and nonzero == 0 
                iszero += 1
                nonzero += 1

        print(nums)

solve = Solution()
solve.moveZeroes(nums = [0,1,0,3,12])
solve.moveZeroes(nums = [0,0,0,0,1])
solve.moveZeroes(nums = [0,0,2,0,1])
solve.moveZeroes(nums = [0,6,0,0,1])
solve.moveZeroes(nums = [1,0])
solve.moveZeroes(nums = [0,1,9,0,0,1,0,0,2,6,0,0,1])

solve.firstattempt(nums = [6, 0])
solve.firstattempt(nums = [0,1,9,0,0,1,0,0,2,6,0,0,1])