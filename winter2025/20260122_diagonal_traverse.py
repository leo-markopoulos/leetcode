def findDiagonalOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    row, col = 0, 0
    for _ in range(len(matrix) * len(matrix[0])):
        result.append(matrix[row][col])
    
        if (row + col) % 2 == 0:
            if col == len(matrix[0]) - 1:
                row += 1
            elif row == 0:
                col += 1
            else:
                row -= 1
                col += 1
        else:
            if row == len(matrix) - 1:
                col += 1
            elif col == 0:
                row += 1
            else:
                row += 1
                col -= 1

    return result