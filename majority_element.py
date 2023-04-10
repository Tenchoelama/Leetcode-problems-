# 169. Majority Element
# Easy
# 14.1K
# 435
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
        
# def majorityElement(nums):
    
#     d = {}
    
#     for num in nums:
#         if num not in d:
#             d[num] = 1
#         else:
#             d[num] += 1
            
#     max_value = max(d.values())
    
#     for key in d:
#         if d[key] == max_value:
#             return key

# print(majorityElement([3,2,3]))
