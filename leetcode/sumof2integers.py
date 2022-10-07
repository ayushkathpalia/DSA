
def getSum(a, b):
    tmp = 0
    while b != 0:
        tmp = (a&b) << 1
        a = a ^ b
        b = tmp
        
    return a
a = -1
b = 1
ans = getSum(a,b)
print(ans)