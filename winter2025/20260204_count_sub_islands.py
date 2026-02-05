def countSubIslands(grid1, grid2):
    visited = set()
    result = 0
    directions = [[1,0], [0,1], [0,-1], [-1,0]]
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if grid2[i][j] == 1 and (i, j) not in visited:
                is_sub_island = True
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    if grid1[x][y] == 0:
                        is_sub_island = False

                    for direction in directions:
                        next_x, next_y = x + direction[0], y + direction[1]
                        if next_x >= 0 and next_x < len(grid1) and next_y >= 0 and next_y < len(grid1[0]) and grid2[next_x][next_y]: 
                            queue.append((next_x, next_y))
                if is_sub_island:
                    result += 1
    return result