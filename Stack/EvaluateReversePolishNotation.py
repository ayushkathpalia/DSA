def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == '-' or token == '+' or token == '*' or token == '/':
            val1 = int(stack.pop())
            val2 = int(stack.pop())
            if token == '-':
                ans = val1 - val2
            elif token == '+':
                ans = val1 + val2
            elif token == '*':
                ans = val1 * val2
            elif token == '/':
                ans = val2 // val1
            stack.append(ans)
        else:
            stack.append(token)
    return ans
arr = ["4","13","5","/","+"]
ans = evalRPN(arr)
print(ans)



print(-101//10)
print(-101/10)
print(int(-101/10))