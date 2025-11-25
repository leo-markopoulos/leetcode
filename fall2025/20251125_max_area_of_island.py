from collections import deque


def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    result = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                queue = deque([(r, c)])
                current_area = 0
                grid[r][c] = 0  
                while queue:
                    cr, cc = queue.popleft()
                    current_area += 1
                    for dr_offset, dc_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = cr + dr_offset, cc + dc_offset
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0 
                            queue.append((nr, nc))
                result = max(result, current_area)
    return result