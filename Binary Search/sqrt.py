def mySqrt(x):
    s = 1
    e = x
    mid = 0
    ans  = -1
    while s <= e:
        mid = int(s+(e-s)/2)
        square = mid*mid
        if square == x:
            return mid
        elif square < x:
            s = mid+1
            ans = mid
        else:
            e = mid-1
    return ans


def more_precise(x,precision,tmpsol):
    ans = tmpsol
    f = 1
    for i in range(precision):
        f = f/10
        j = ans
        while(j*j < x):
            ans = j
            j+=f
 
    return round(ans,precision)
n = 37
ans =mySqrt(n)
res = more_precise(n,3,ans)
print(res)

