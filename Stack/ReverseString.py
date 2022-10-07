s= "ayush"

stack = []
ans = ""
for char in s:
    stack.append(char)

print(stack)

while stack:
    char = stack.pop()
    ans+=char

print(ans)
