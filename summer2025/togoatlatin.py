def toGoatLatin(sentence):

  words = sentence.split(' ')

  for i in range(len(words)):
    if not words[i][0] in 'aeiouAEIOU':
      words[i] = words[i] + words[i][0]
      words[i] = words[i][1:]
    words[i] = words[i] + 'maa' + 'a'*i

  return ' '.join(words)
