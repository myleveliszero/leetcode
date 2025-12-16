def removeElement(nums, val: int) -> int:
    left, right = 0, 0
    while right < len(nums):
        if nums[right] == val:
            while right < len(nums) and nums[right] == val:
                right += 1
        else:
            nums[left] = nums[right]
            left, right = left+1, right+1 

    return left 

print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
print(removeElement(nums = [3,2,2,3], val = 3))
            