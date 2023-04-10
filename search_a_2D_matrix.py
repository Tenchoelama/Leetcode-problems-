# 74. Search a 2D Matrix
# Medium
# 11.8K
# 342
# Companies
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

def Search2DMatrix(matrix, target):
    
        
    for e in matrix:
        l = 0
        h = len(e) - 1
        
        
        while l <= h:
            mid = (l + h) // 2
            if e[mid] == target:
                return True 
            elif e[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

    return False
        
        
    
    
print(Search2DMatrix( [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))