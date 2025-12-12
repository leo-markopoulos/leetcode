def findBall(grid):
    result = [0] * len(grid[0])
    for ball in range(len(grid[0])):
        col = ball
        stuck = False
        for row in range(len(grid)):
            direction = grid[row][col]
            next_col = col + direction
            if next_col < 0 or next_col >= len(grid[0]) or grid[row][next_col] != direction:
                stuck = True
                break 
            col = next_col

        if stuck:
            result[ball] = -1
        else:
            result[ball] = col 

    return result
