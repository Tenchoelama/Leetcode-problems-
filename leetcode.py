import math


# 198. House Robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
# you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.


# def robber(nums):
    
#     rob1 = 0
#     rob2 = 0
    
#     for num in nums:
#         temp = max(num + rob1, rob2)
#         rob1 = rob2
#         rob2 = temp
        
#     return rob2
   


# print(robber([1,2,3,1]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------
    
 
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
    
    
# def singleNumber(nums):
    
#     result = 0
#     for num in nums:
#         result ^= num # ^ is a binary operator that compares two bits and 
#                       # returns 1 if they are different, and 0 if they are the same.
#     return result
    
# print(singleNumber([4,1,2,1,2]))   


# -----------------------------------------------------------------------------------------------------------------------------------------------------------
    
# 402. Remove K Digits
# Medium
# 7.3K
# 308
# Companies
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest


# def removeKDigits(num, k):
    
#    stack = []
   
#    for digit in num:
       
#        if stack and k and digit < stack[-1]:
#            stack.pop()
#            k -= 1
           
#        stack.append(digit)
       
#    if k:
#         answerstack = answerstack[:-k]
        
#    return ''. join(stack)
        
        

# print(removeKDigits("10200", 1))
#------------------------------------------------------------------------------------------------------

# 70. Climbing Stairs
# Easy
# 17.5K
# 540
# Companies
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# def climb(n):
    
    
#     a, b = 0, 1
    
#     for i in range(n):
#         a, b = b, a + b
#     return b

# print(climb(3))

#----------------------------------------------------------------------------------------------------------------------


# 7. Reverse Integer
# Medium
# 10.1K
# 11.8K
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321


# def reverseInteger(num):
    
    # max_int = 2**31 -1
    # min_int = -2**31
    
    # if num == 0:
    #     return 0 
    
    # if num < 0:
    #     str_num = str(num)
    #     str_num1 = str_num[0]
    #     temp = str_num.replace('-',"")
    #     temp = temp[::-1]
    #     str_num1 += temp 
    #     after = int(str_num1)
    #     if after > max_int or  after < min_int:
    #         return 0
    #     else:
    #         return after
        
    # else:
    #     before = str(num)  
    #     after = int("".join(reversed(before)))
    #     if after > max_int or  after < min_int:
    #         return 0
    #     else:
    #         return after
    
    
# print(reverseInteger(-123))

#--------------------------------------------------------------------------------------------------------------------

# 283. Move Zeroes
# Easy
# 13.1K
# 330
# Companies
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# def moveZeroes(nums):
    
#     j = 0
    
#     for i in range(len(nums)):
        
#         if nums[i] != 0:
            
#             nums[i], nums[j] = nums[j], nums[i]
            
#             j += 1

#     return nums

# print(moveZeroes([0,1,0,3,12]))   
            
#---------------------------------------------------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------------------------------------

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

# def missingNum(nums):
    
#     n = len(nums)
#     num_set = set(nums)
#     l = []
    
#     for num in range(1, n+1):
#         if num not in num_set:
#             l.append(num)
        
#     return l 
            
# print(missingNum([4,3,2,7,8,2,3,1]))
    
#-------------------------------------------------------------------------------------------------------------------------------------------------

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
        
#-------------------------------------------------------------------------------------------------------------------------------


# 14. Longest Common Prefix
# Easy
# 13.2K
# 3.8K
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# def commonPrefix(strs):
    
#     res = ''
    
#     for i in range(len(strs[0])):
#         for s in strs:
#             if i == len(s) or s[i] != strs[0][i]:
#                 return res
        
#         res += strs[0][i]
        
#     return res
    

# print(commonPrefix(["flower","flow","flight"]))


#---------------------------------------------------------------------------------

# 1672. Richest Customer Wealth
# Easy
# 3.3K
# 321
# Companies
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.


# def richestWealth(accounts):
    
#     d = {}
    
#     for i, elem in enumerate(accounts):
#         d[i] = sum(elem)
        
#     return max(d.values())
    
    
# print(richestWealth([[1,5],[7,3],[3,5]]))
    
#-------------------------------------------------------------------------------------------

# 2373. Largest Local Values in a Matrix
# Easy
# 510
# 49
# Companies
# You are given an n x n integer matrix grid.

# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

# Return the generated matrix.


# Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]

# [9,9,8,1]
# [5,6,2,6]
# [8,2,6,4]
# [6,2,2,2]


# def largestMatrix(grid):
    
#     col = row = len(grid)-2
#     temp_l = []
#     l = []
#     for i in range(row):
#         for j in range(col):
#             t = 0
#             for k in range(i,i+3):
#                 temp = max(grid[k][j:j+3])
#                 t = max(t,temp)
#             temp_l.append(t)
#         l.append(temp_l)
#         temp_l = []
#     return l
            
    
    
# print(largestMatrix([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))

#---------------------------------------------------------------------------------------------------------------

# 54. Spiral Matrix
# Medium
# 10.8K
# 1K
# Companies
# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# def spiralMatrix(matrix):
    
#     res = []
#     l , r = 0, len(matrix[0])
#     top, bottom = 0, len(matrix)
    
#     while l < r and top < bottom:
#         #get every i in the top row
#         for i in range(l,r):
#             res.append(matrix[top][i])
#         top += 1
        
#         #get every i in the right col
#         for i in range(top, bottom):
#             res.append(matrix[i][r -1])
#         r -= 1
        
#         if not (l<r and top < bottom):
#             break 
        
#         #get every i in the bottom row 
#         for i in range(r-1, l-1,-1):
#             res.append(matrix[bottom-1][i])
#         bottom -= 1
        
#         #get every i in the left col
#         for i in range(bottom-1, top -1,-1):
#             res.append(matrix[i][l])
#         l += 1
        
#     return res
        
        
        
# print(spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))

#-------------------------------------------------------------------------------------------------------------------

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

# def Search2DMatrix(matrix, target):
    
        
#     for e in matrix:
#         l = 0
#         h = len(e) - 1
        
        
#         while l <= h:
#             mid = (l + h) // 2
#             if e[mid] == target:
#                 return True 
#             elif e[mid] < target:
#                 l = mid + 1
#             else:
#                 h = mid - 1

#     return False
        
        
    
    
# print(Search2DMatrix( [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))

#--------------------------------------------------------------------------------------------------

# 36. Valid Sudoku
# Medium
# 8.3K
# 886
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

#three differnet ways to solve this problem used (shown seperately in row, column and grid sections)
# def validSukudo(board):

#     #row
#     row = []
#     for r in board:
#         for j in r:
#             if j == '.':
#                 continue 
#             if j not in row:
#                 row.append(j)
#             else:
#                 return False 
#         row = []   
    
#     #column
#     for c in range(9):
#         col = []
#         for r in range(9):
#             if board[r][c] != ".":
#                 col.append(board[r][c])
#             if len(col) != len(set(col)):
#                 return False 
                
                
#     #grid
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             nums = []
#             for r in range(i, i+3):
#                 for c in range(j, j+3):
#                     num = board[r][c]
#                     if num == '.':
#                         continue
#                     if num in nums:
#                         return False
#                     nums.append(num)
            
#     return True 
            
    
# print(validSukudo([[".",".",".",".","5",".",".","1","."],
#                    [".","4",".","3",".",".",".",".","."],
#                    [".",".",".",".",".","3",".",".","1"],
#                    ["8",".",".",".",".",".",".","2","."],
#                    [".",".","2",".","7",".",".",".","."],
#                    [".","1","5",".",".",".",".",".","."],
#                    [".",".",".",".",".","2",".",".","."],
#                    [".","2",".","9",".",".",".",".","."],
#                    [".",".","4",".",".",".",".",".","."]]))

#----------------------------------------------------------------------------------------------





