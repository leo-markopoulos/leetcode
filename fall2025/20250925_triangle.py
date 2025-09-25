from collections import deque

def minimumTotal(triangle):
    optimal_cell_path = {}
    optimal_cell_path[(0, 0)] = triangle[0][0]
    queue = deque([(0, 0, triangle[0][0])])
    min_path = float('inf')

    while queue:
        row, col, current_sum = queue.popleft()
        if row == len(triangle) - 1:
            min_path = min(min_path, current_sum)
            continue

        for i in range(2):
            next_row = row + 1
            next_col = col + i
            next_sum = current_sum + triangle[next_row][next_col]

            if (next_row, next_col) not in optimal_cell_path or next_sum < optimal_cell_path[(next_row, next_col)]:
                optimal_cell_path[(next_row, next_col)] = next_sum
                queue.append((next_row, next_col, next_sum))

    return min_path
