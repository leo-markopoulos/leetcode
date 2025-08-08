def romanToInt(s):
  result = 0
  i = 0
  romannums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  while i < len(s):
    if i + 1 < len(s) and romannums.get(s[i]) < romannums.get(s[i+1]):
      result += romannums.get(s[i+1]) - romannums.get(s[i])
      i += 2
    else:
      result += romannums.get(s[i])
      i += 1
  return(result)