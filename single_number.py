# 136. Single Number
# Easy
# 13.3K
# 512
# Companies
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
    
    
def singleNumber(nums):
    
    result = 0
    for num in nums:
        result ^= num # ^ is a binary operator that compares two bits and 
                      # returns 1 if they are different, and 0 if they are the same.
    return result
    
print(singleNumber([4,1,2,1,2]))   
