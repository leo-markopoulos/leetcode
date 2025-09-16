def leastBricks(wall):
    for row in range(len(wall)):
        for brick in range(1,len(wall[row])):
            wall[row][brick] += wall[row][brick-1] 
            
    edges = []
    for row in wall:
        edges.extend(row[:-1])
            
    if not edges:
        return len(wall)
    else:
        return len(wall) - edges.count(max(set(edges), key=edges.count))