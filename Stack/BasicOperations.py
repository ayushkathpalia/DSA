# #Using LIST

# stack = []

# stack.append('a')
# stack.append(10)

# #peek
# print(stack[-1])

# #stack.pop()
# print(len(stack))

# #stack.pop()

# if stack:
#     print('not empty')
# else:
#     print('empty')


#---------------------------------------
#USING DEQUE - Double Ended Queue

from collections import deque
 
stack = deque()
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack:')
print(stack)

print('\nPeaking')
print(stack[-1])


# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 