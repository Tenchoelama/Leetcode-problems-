# 448. Find All Numbers Disappeared in an Array
# Easy
# 8.2K
# 428
# Companies
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]

def missingNum(nums):
    
    n = len(nums)
    num_set = set(nums)
    l = []
    
    for num in range(1, n+1):
        if num not in num_set:
            l.append(num)
        
    return l 
            
print(missingNum([4,3,2,7,8,2,3,1]))