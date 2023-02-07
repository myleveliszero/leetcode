# Status: Not Bad

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Note:
        nums = "----->-->"; k = 3
        result = "-->----->";
        reverse "----->-->" we can get "<--<-----"
        reverse "<--" we can get "--><-----"
        reverse "<-----" we can get "-->----->"
        """
        def myrevers(arr, left, right):
            while left < right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1
        
        k %= len(nums)

        myrevers(nums, 0, len(nums)-1)
        myrevers(nums, 0, k-1)
        myrevers(nums, k, len(nums)-1)

        print(nums)


      

solve = Solution()

solve.rotate(nums = [1,2], k = 3)
solve.rotate(nums = [1,2,3,4,5,6,7,8,9], k = 4)
solve.rotate(nums = [1,2,3,4,5,6,7], k = 3)
solve.rotate(nums = [-1,-100,3,99], k = 2) 
