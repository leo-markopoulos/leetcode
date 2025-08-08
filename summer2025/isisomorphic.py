def isIsomorphic(s, t):
  if len(s) != len(t):
    return False

  Hash = {}
  Seen = {}

  for i in range(len(s)):
    if s[i] not in Hash:
      if t[i] in Seen:
        return False
      Hash[s[i]] = t[i]
      Seen[t[i]] = s[i]
    elif Hash[s[i]] != t[i]:
      return False
  return True
