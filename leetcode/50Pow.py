
from re import S


def myPow(x: float, n: int) -> float:
    ans = 1
    def helper(x,n,ans):
        if n == 0:
            return  
        ans *= x
        helper(x,n-1,ans)
    helper(x,n,ans)
    print(ans)


myPow(2.0,10)


print(ord(' '))