# Status: Good(99/100)

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]  == [1,2,1]+[1,2,1] = [1,2,1,1,2,1]
# Input: nums = [1,1]
# Output: [1,1,1,1]  == [1,1] + [1,1] = [1,1,1,1]

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
       # return nums*2
       # return nums+nums
        nums.extend(nums)
        return nums
    def version2(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
       # for i in nums:
       #     nums.append(i) # loop will be infinite 
       # return nums 

solve = Solution()
print(solve.getConcatenation([1,2,3]))
print(solve.version2([1,1,2]))
print(solve.version2([0,0,1,1,2]))


