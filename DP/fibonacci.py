 #Top Down Approach -> Recursion + Memorization

def fib1(n):
    dp = [-1]*(n+1)
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib1(n-1) + fib1(n-2)
    return dp[n]
#O(n),O(n)

#Bottom Up->Tabulation
def fib2(n):
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
#O(n),O(n)

#Optimized ->
def fib3(n):
    prev1 = 0
    prev2 = 1
    
    for i in range(2,n+1):
        tmp = prev2
        prev2 = prev1+prev2
        prev1 = tmp 
    return prev2

#O(n),O(1)
ans=fib3(8)
print(ans)