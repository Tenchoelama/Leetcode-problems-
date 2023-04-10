# 54. Spiral Matrix
# Medium
# 10.8K
# 1K
# Companies
# Given an m x n matrix, return all elements of the matrix in spiral order.

 

def spiralMatrix(matrix):
    
    res = []
    l , r = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    while l < r and top < bottom:
        #get every i in the top row
        for i in range(l,r):
            res.append(matrix[top][i])
        top += 1
        
        #get every i in the right col
        for i in range(top, bottom):
            res.append(matrix[i][r -1])
        r -= 1
        
        if not (l<r and top < bottom):
            break 
        
        #get every i in the bottom row 
        for i in range(r-1, l-1,-1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        
        #get every i in the left col
        for i in range(bottom-1, top -1,-1):
            res.append(matrix[i][l])
        l += 1
        
    return res
        
        
        
print(spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))