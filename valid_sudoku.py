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
