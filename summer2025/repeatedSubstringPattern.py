def repeatedSubstringPattern(s):
    for i in range(1,len(s)//2+1):
        s_list = []

        for j in range(0, len(s), i):
            s_list.append(s[j:j+i])

        x = s_list.pop(0)
        while True:
            if not s_list:
                return True
            elif s_list.pop(0) != x:
                break

    return False     
