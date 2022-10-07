#Basically for the minimum cost tree from Leaf Values, you want the smallest values farthest down 
#the root, as you go up the tree, the leaf values should stay the same or increase. 
#The tree should  look like a flatten binarty tree except each node needs 0 or two leafs.  IE given [8,4,2,3] 
#
#        32
#       /  \
#      12   8
#     / \
#    6   4
#   / \
#  2  3
# 
# Result = 50
#have a monotone stack that keeps a decreasing order of values
#if we get a bigger number or equal then what is on top of the stack
#then we pop it off. And add whatever the value we popped off is  times the  min
#of ether whhats  on top of the stack or the number itself. 
#Keep doing this process til we can add num to the stack and it will still be in decreasing order
#After iterating through arr, if the stack still has more than 2 values in it 
#then pop off what is on top of the stack and
#times it by the next thing on the stack until there or two or less values.

#IE if given [6,4,2] res would be 0 after iterating through arr, but stack would be ['INF',6,4,2] so it would be
# (6*4) + (2*4) = 32

from re import A


def mctFromLeafValues(arr):
    stack =  [float('inf')]
    res = 0
    
    for num in arr:
        while stack and stack[-1] <= num:
            cur = stack.pop()
            #stack will always have atleast one thing in it after pop because inf is in there
            res += cur * min(num, stack[-1])
            
        stack.append(num)
    while len(stack) > 2:
        res += stack.pop() * stack[-1]
    
    return res
ans = mctFromLeafValues([6,2,4])
print(ans)