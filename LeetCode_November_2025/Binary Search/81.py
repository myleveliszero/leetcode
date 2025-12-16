def search(nums, target: int) -> bool:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (right-left)//2 + left
        if nums[mid] == target:
            return True
        elif nums[left] == nums[mid] and nums[right] == nums[mid]:
            left = left + 1
            right = right - 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        elif nums[mid] <= right:
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else: 
                right = mid-1
        
    return False
        
print(search([1,0,1,1,1], target=0))
print(search([1,2,1], target=1))
print(search([1,1,1,0,1], target=0))
print(search([1,1,1,1,1,1,0,0,1,1], target=0))
print(search([1,1,0,0,1,1,1,1,1,1], target=0))

print(search([5,1,3], target=3))
print(search([4,5,6,7,0,1,2], target=0))

print(search([4,5,6,7,8,9,10,11,12,0,1,2], target=2))

print(search([6,7,8,9,10,11,12,13,14,0,1,2,4,5], target=14))