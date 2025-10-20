def onesMinusZeros(grid):
    rows = []
    for r in grid:
        row_total = 0
        for c in r:
            if c == 0:
                row_total -= 1
            else: 
                row_total += 1
        
        rows.append(row_total)
    
    cols = []
    for c in range(len(grid[0])):
        col_total = 0
        for r in range(len(grid)):
            if grid[r][c] == 0:
                col_total -= 1
            else: 
                col_total += 1
        
        cols.append(col_total)
    
    diff = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for c_ind, c in enumerate(cols):
        for r_ind, r in enumerate(rows):
            diff[r_ind][c_ind] = r + c
    
    return diff