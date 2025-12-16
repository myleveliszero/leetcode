def twoSum(numbers, target: int):
    left, right = 0, (len(numbers)-1)       
    while left <= right:
        sum = numbers[left] + numbers[right]  
        if sum == target:
            return [left+1,right+1]
        elif sum < target:
            left += 1
        else:
            right -= 1
        
   
print(twoSum([1,3,4,6,7,9], target=5))
print(twoSum([1,3,4,6,7,9], target=8))
print(twoSum([1,3,4,6,7,9], target=11))
print(twoSum([1,3,4,6,7,9], target=16))

print(twoSum([1,2,3,4,5,6,7,8,9], target=3))
print(twoSum([1,2,3,4,5,6,7,8,9], target=16))
print(twoSum([1,2,3,4,5,6,7,8,9], target=17))
