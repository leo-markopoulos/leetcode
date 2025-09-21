def longestValidParentheses(s):
    best = 0
    stack = [-1] 
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else: 
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                current_length = i - stack[-1]
                best = max(best, current_length)
    
    return best