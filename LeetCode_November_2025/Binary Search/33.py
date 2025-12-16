def search(nums, target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        m = (r-l)//2 + l
        if nums[m]==target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r=m-1
            else:
                l = m+1
        else:
            if nums[m] < target <= nums[r]:
                l = m+1
            else:
                r = m-1
    return -1

print(search([5,1,3], target=3))
# print(search([4,5,6,7,0,1,2], target=0))

# print(search([4,5,6,7,8,9,10,11,12,0,1,2], target=2))

# print(search([6,7,8,9,10,11,12,13,14,0,1,2,4,5], target=14))