'''
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

'''


from cmath import inf


def coinChange(coins,amount):
    def helper(target):
        #base case
        if target == 0:
            return 0 
        if target < 0:
            return inf
        
        minimum = inf
        for i in range(len(coins)):
            ans = helper(target-coins[i])
            if ans != inf:
                minimum = min(minimum,1+ans)  #1+  because considering the current coin
        return minimum

    result = helper(amount)
    if result == inf:
        print('-1')
    print(result)


#TOP DOWN

def coinChange2(coins,amount):
    def helper(target,dp):
        #base case
        if target == 0:
            return 0 
        if target < 0:
            return inf
        if dp[target] != -1:
            return dp[target]

        minimum = inf
        for i in range(len(coins)):
            ans = helper(target-coins[i],dp)
            if ans != inf:
                minimum = min(minimum,1+ans)  #1+  because considering the current coin
        dp[target] = minimum  
        return minimum

    dp = [-1]*(amount+1)
    result = helper(amount,dp)
    if result == inf:
        print('-1')
    print(result)


#bottom up

def coinChange3(coins,amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    for a in range(1,amount+1):
        for c in coins:
            if a-c >= 0:
                dp[a] = min(dp[a],1+dp[a-c])
    if dp[amount] != amount+1:
        return dp[amount]
    else:
        return -1
coins = [1,2,5]
amount = 11
ans = coinChange3(coins,amount)
print(ans)