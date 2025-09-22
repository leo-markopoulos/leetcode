from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)
        path = [board[i][j if (n-1-i)%2==0 else n-1-j] for i in range(n-1, -1, -1) for j in range(n)]

        queue = deque([(0, 0)])
        visited = set([0])

        while queue:
            pos, moves = queue.popleft()
            if pos == n * n - 1:
                return moves

            for dice in range(1, 7):
                new_pos = pos + dice
                if new_pos >= n * n:
                    continue
                if path[new_pos] != -1:
                    new_pos = path[new_pos] - 1
                if new_pos not in visited:
                    visited.add(new_pos)
                    queue.append((new_pos, moves + 1))

        return -1