def isPalindromeAlphaNumeric(s):
  abcs = 'abcdefghijklmnopqrstuvxyz0123456789'
  ABCs = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
  s = list(s)
  for i in range(len(s)):
    if s[i] in ABCs:
      s[i] = abcs[ABCs.index(s[i])]
    elif not s[i] in abcs:
      s[i] = ' '

  s = ''.join(s)
  s = s.split(' ')
  s = ''.join(s)

  for i in range(len(s)):
    if not s[i] == s[-(i+1)]:
      return False
  return True
