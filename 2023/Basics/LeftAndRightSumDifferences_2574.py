# Status: Not Bad

class Solution:
    def leftRigthDifference(self, nums):
        ans = [0]*len(nums)
        leftSum = [0]
        rightSum = [0]
        for i in range(len(nums)-1):
            leftSum.append(nums[i]+leftSum[-1])
            rightSum.append(nums[~i]+rightSum[-1])
        rightSum = rightSum[::-1]
        for i in range(len(ans)):
            ans[i] = abs(leftSum[i]-rightSum[i])
        return ans

solve = Solution()
print(solve.leftRigthDifference([10,4,8,3]))