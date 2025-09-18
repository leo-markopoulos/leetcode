def maxIncreaseKeepingSkyline(grid):
    result = 0
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            result += min(max(grid[row]), max([c[col] for c in grid])) - grid[row][col]       
    return result  