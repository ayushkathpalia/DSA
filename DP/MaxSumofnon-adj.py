#recursion
def maximumNonAdjacentSum(nums):    
    def helper(n):
        #base case
        if n == 0:
            return nums[0]
        if n < 0:
            return 0
        
        incl = helper(n-2)+nums[n]
        exl = helper(n-1)+0
        return max(incl,exl)
    n = len(nums)
    return helper(n-1)

#top  down

def maximumNonAdjacentSum(nums):    
    def helper(n,dp):
        #base case
        if n == 0:
            return nums[0]
        if n < 0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        incl = helper(n-2,dp)+nums[n]
        exl = helper(n-1,dp)+0
        dp[n] =  max(incl,exl)
        return dp[n]
    
    n = len(nums)
    dp = [-1]*n
    return helper(n-1,dp)

#bottom up
def maximumNonAdjacentSum(nums):    
    #base case
    n = len(nums)
    dp = [0]*(len(nums))
    dp[0] = nums[0]

    for i in range(1,len(nums)):
        incl = dp[i-2]+nums[i]
        exl = dp[i-1]+0
        dp[i] = max(incl,exl)
    return dp[n-1]

#bottom up optimized
def maximumNonAdjacentSum(nums): 
    #base case
    prev1 = nums[0]
    prev2 = 0
    for i in range(1,len(nums)):
        incl = prev2+nums[i]
        exl = prev1+0
        ans = max(incl,exl)
        prev2 = prev1
        prev1 = ans
    return prev1