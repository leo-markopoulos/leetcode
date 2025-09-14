from collections import deque

def orangesRotting(grid): 
    rows, cols = len(grid), len(grid[0])
    rotten_oranges = deque()
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                rotten_oranges.append([row, col])
                grid[row][col] = 0 

    result = -1
    while rotten_oranges:
        for _ in range(len(rotten_oranges)):
            rot = rotten_oranges.popleft()
            if rot[0]-1 >= 0 and grid[rot[0]-1][rot[1]] == 1:
                grid[rot[0]-1][rot[1]] = 2
                rotten_oranges.append([rot[0]-1, rot[1]])
            if rot[1]-1 >= 0 and grid[rot[0]][rot[1]-1] == 1:
                grid[rot[0]][rot[1]-1] = 2
                rotten_oranges.append([rot[0], rot[1]-1]) 
            if rot[0]+1 < rows and grid[rot[0]+1][rot[1]] == 1:
                grid[rot[0]+1][rot[1]] = 2
                rotten_oranges.append([rot[0]+1, rot[1]])
            if rot[1]+1 < cols and grid[rot[0]][rot[1]+1] == 1:
                grid[rot[0]][rot[1]+1] = 2
                rotten_oranges.append([rot[0], rot[1]+1])
        result += 1

    if any(1 in sublist for sublist in grid):
        return -1
    elif result < 0:
        return 0
    else:
        return result