# 55. Jump Game
# Medium
# 15.9K
# 814
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

def jump(nums):
    
    n = len(nums)
    p1 = 0
    
    # iterate until we reach the end of the list
    while p1 < n:
        # if we have reached the end of the list, return True
        if p1 == n - 1:
            return True
        
        # if the maximum jump length at the current position is 0, we can't move forward
        if nums[p1] == 0:
            return False
        
        # find the maximum jump length from the current position
        max_jump = 0
        for i in range(1, nums[p1] + 1):
            if p1 + i < n and nums[p1 + i] + i > max_jump:
                max_jump = nums[p1 + i] + i
        
        # jump to the next position
        p1 = p1 + max_jump - 1
        
    # we have reached the end of the list, so return True
    return True

print(jump([2,3,1,1,4]))
