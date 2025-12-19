from collections import deque

def shortestBridge(grid):
    n = len(grid)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visited = [[False]*n for _ in range(n)]
    queue = deque()
    
    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= n:
            return
        if visited[r][c] or grid[r][c] == 0:
            return
        
        visited[r][c] = True
        queue.append((r, c))
        
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    
    found = False
    for i in range(n):
        if found:
            break
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                found = True
                break
    
    flips = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if grid[nr][nc] == 1:
                        return flips
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        
        flips += 1