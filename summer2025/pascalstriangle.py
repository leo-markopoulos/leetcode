def pascalsTriangle(numRows):
  result = []
  for i in range(numRows):
    result.append([1])
    for j in range(i-1):
      result[-1].append(result[-2][j]+result[-2][j+1])
    if i != 0:
      result[-1].append(1)
  return result
