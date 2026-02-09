def simplifiedFractions(n):
    visited = {}
    result = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i/j not in visited:
                visited[i/j] = 1
                result.append(f"{i}/{j}")
    return result