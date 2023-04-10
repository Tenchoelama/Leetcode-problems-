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
