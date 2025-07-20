def lengthOfLongestSubstring(s: str) -> int:
  result = []
  sub = 0
  for i in range(len(s)):
    if s[i] not in result:
      result.append(s[i])
      if sub < len(result):
        sub = len(result)
    else:
      result = result[result.index(s[i]) + 1:]
      result.append(s[i])
  return sub
