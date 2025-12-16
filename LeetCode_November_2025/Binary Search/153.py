def findMin(nums) -> int:
    left, right = 0, len(nums)-1
    while left < right:
        mid = (right-left)//2 + left
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid+1
    return nums[left]
    
print(findMin([5,1,3]))
print(findMin([2,1]))

print(findMin(nums = [11,13,15,17]))

print(findMin([4,5,6,7,8,9,10,11,12,0,1,2]))

print(findMin([6,7,8,9,10,11,12,13,14,0,1,2,4,5]))