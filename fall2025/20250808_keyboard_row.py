def findWords(words):
    rows = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
    result = []
    for w in words:
        for r in rows:
            if all(c in r for c in w):
                result.append(w)
                break
    return result