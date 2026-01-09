def gameOfLife(board):
    result = [[] for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board[0])): 
            neighbors = 0
            for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                if 0 <= x+dc < len(board[0]) and 0 <= y+dr < len(board):
                    neighbors += board[y+dr][x+dc]

            if board[y][x] == 1:
                if neighbors not in [2,3]:
                    result[y].append(0)
                else:
                    result[y].append(1)
            
            if board[y][x] == 0:
                if neighbors == 3:
                    result[y].append(1)
                else:
                    result[y].append(0)

    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] = result[y][x]