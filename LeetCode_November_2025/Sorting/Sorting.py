from random import randrange

def QuickSort(nums, left, right):
    if right-left <= 0:
        return nums
    idx = randrange(left, right)
    nums[right], nums[idx] = nums[idx], nums[right]
    
    pivot = nums[right]
    lp = rp = left
    while rp < right:
        if nums[rp] <= pivot:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
        rp += 1

    nums[lp], nums[right] = nums[right], nums[lp]
    QuickSort(nums, left, lp-1)
    QuickSort(nums, lp+1, right)

    return nums

def QuickSortModified(nums, left, right):
    if right-left <= 0:
        return nums
    idx = randrange(left, right)
    nums[right], nums[idx] = nums[idx], nums[right]
    
    pivot = nums[right]
    lp = rp = left
    while rp < right:
        if nums[rp] < pivot:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
        rp += 1
    
    lp = rp = left
    while rp < right:
        if nums[rp] <= pivot:
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp += 1
        rp += 1
    
    nums[lp], nums[right] = nums[right], nums[lp]
    llp = left
    while llp < lp:
        if nums[llp] == pivot:
            break
        llp += 1


    QuickSortModified(nums, left, llp-1)
    QuickSortModified(nums, lp+1, right)

    return nums


# nums = [6, 2, 4, 1, 3] 
# nums = [2,3,3,3,3,6,3,3,3,4,3,1,3] 
# nums = [-2463, -9477, -7841, -4443, -1212, 333, 687, 7155]
nums = [6585, 8045, -373, -715, 8045, 9704]

print(QuickSortModified(nums, 0, len(nums)-1))
   

def MergeSort(nums, left, right):
    if right-left <= 0:
        return nums[left:right+1]
    i = (right+left)//2
    part1 = MergeSort(nums, left, i)
    part2 = MergeSort(nums, i+1, right)
    new_arr = []
    lp, rp = 0, 0 # lp=leftpointer
    while lp < len(part1) and rp < len(part2):
        if part1[lp] <= part2[rp]:
            new_arr.append(part1[lp])
            lp += 1
        else:
            new_arr.append(part2[rp])
            rp += 1
    while lp < len(part1): 
        new_arr.append(part1[lp]); 
        lp += 1
    while rp < len(part2):
        new_arr.append(part2[rp])
        rp += 1 

    return new_arr

# nums = [3,2,4,1,6] 
# print(MergeSort(nums, 0, len(nums)))


# Time complexity O(n^2)
# Space complexity O(1)
def insetionSort(nums):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
    return nums

def test(func1, func2, a, b):
    size = randrange(1, 1000)
    nums = [randrange(a, b) for _ in range(size)]
    res1 = func1(nums)
    # res2 = func2(nums, 0, len(nums))
    res2 = func2(nums, 0, len(nums)-1)
    if res1 != res2:
        print(nums)
        print(res1)
        print(res2)
        return True

for i in range(1000):
    print(i)
    if test(sorted, QuickSortModified, a=-202, b=404):
        break