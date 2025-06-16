def twoSum(nums, target):
    seen = {} 

    for index, num in enumerate(nums):
        find = target - num  

        if find in seen:
            return [seen[find], index]  
        seen[num] = index 

nums = [2, 7, 11, 15]
target = 9
print("Output:", twoSum(nums, target))  
