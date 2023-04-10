# 581. Shortest Unsorted Continuous Subarray
# Medium
# 7.2K
# 246
# Companies
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


# def shortestSubarray(nums):
    
    
#     nums1 = sorted(nums)
    
#     i = 0
#     while i < len(nums) and nums[i] == nums1[i]:
#         i += 1
        
#     j = len(nums)-1 
#     while j >= 0 and nums[j] == nums1[j]:
#         j -= 1
        
#     return j -i + 1
        
        
    
    
# print(shortestSubarray([2,6,4,8,10,9,15]))
                       #2,4,6,8,9,10,15     