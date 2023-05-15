def island(grid):
    
    p = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    p += 1
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    p += 1
                if j == 0  or grid[i][j-1] == 0:
                    p += 1
                if j == len(grid[i])-1 or grid[i][j+1] == 0:
                    p += 1
    
    return p
            




print(island([[0,1,0,0],
              [1,1,1,0],
              [0,1,0,0],
              [1,1,0,0]]))