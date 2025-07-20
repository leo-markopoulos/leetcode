def addBinary(a , b):
  a = list(a)[::-1]
  b = list(b)[::-1]
  anum = 0
  bnum = 0

  for i in range(len(a)):
    if a[i] == '1':
      anum += 2**i

  for i in range(len(b)):
    if b[i] == '1':
      bnum += 2**i

  result = []
  total = anum + bnum
  i = 1

  if total == 0:
    return '0'

  while total >= i:
    i *= 2
  i //= 2


  while i > 0:
    if total >= i:
      result.append('1')
      total -= i
    else:
      result.append('0')
    i //= 2

  return ''.join(result)
