def searchMatrix(matrix, target):
    i = 0
    j = 0
    while i < len(matrix):
        if matrix[i][j] == target: 
            return True
        elif matrix[i][0] > target:
            return False
        elif matrix[i][j] > target or j+1 >= len(matrix[i]):
            i += 1
            j = 0
        else:
            j += 1
    return False