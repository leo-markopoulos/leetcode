def minimumArea(grid):
    rows = []
    for row in grid:
        if 1 in row:
            rows.append(1) 
        else: 
            rows.append(0)  

    top = 0
    while top < len(rows) and rows[top] == 0:
        top += 1
    bottom = len(rows) - 1
    while bottom >= 0 and rows[bottom] == 0:
        bottom -= 1
    
    grid_2 = []
    for i in range(len(grid[0])):
        grid_2.append([])
        for j in range(len(grid)):
            grid_2[i].append(grid[j][i])
    
    columns = []
    for column in grid_2:
        if 1 in column:
            columns.append(1)
        else: 
            columns.append(0)

    left = 0
    while left < len(columns) and columns[left] == 0:
        left += 1
    right = len(columns) - 1
    while right >= 0 and columns[right] == 0:
        right -= 1
    
    return (bottom - top + 1) * (right - left + 1)