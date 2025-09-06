def numIslands(grid):   
    def clearIsland(xcord, ycord): 
        if ycord < 0 or xcord < 0 or ycord >= len(grid) or xcord >= len(grid[0]) or grid[ycord][xcord] == '0':
            return
        grid[ycord][xcord] = '0'
        clearIsland(xcord + 1, ycord)
        clearIsland(xcord - 1, ycord)
        clearIsland(xcord, ycord + 1)
        clearIsland(xcord, ycord - 1)
        
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '1':
                result += 1
                clearIsland(x, y)

    return result
