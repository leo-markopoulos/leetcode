from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        dominoes = list(dominoes)
        queue = deque()

        for i, d in enumerate(dominoes):
            if d != '.':
                queue.append((i, d))

        time = [0] * n
        forces = [None] * n 
        while queue:
            i, d = queue.popleft()

            if d == 'L' and i > 0:
                ni = i - 1
            elif d == 'R' and i < n - 1:
                ni = i + 1
            else:
                continue

            if dominoes[ni] == '.':
                dominoes[ni] = d
                time[ni] = time[i] + 1
                forces[ni] = d
                queue.append((ni, d))
            elif dominoes[ni] != '.' and dominoes[ni] != d:
                if time[ni] == time[i] + 1:
                    dominoes[ni] = '.'

        return ''.join(dominoes)