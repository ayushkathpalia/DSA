# def minCostClimbingStairs(cost):
#     def helper(index):
#         if index == 0:
#             return cost[0]
#         if index == 1:
#             return cost[1]
#         ans = cost[index] +min(helper(index-1),helper(index-2))
#         return ans
#     n = len(cost)
#     ans = min(helper(n-1),helper(n-2))
#     print(ans)

#TOP down -> O(n),O(n)

# def minCostClimbingStairs2(cost):
#     def helper(index,dp):
#         if index == 0:
#             return cost[0]
#         if index == 1:
#             return cost[1]
#         if dp[index] != -1:
#             return dp[index]
#         dp[index] = cost[index] +min(helper(index-1,dp),helper(index-2,dp))
#         return dp[index]

#     n = len(cost)
#     dp = [-1]*(n+1)
#     ans = min(helper(n-1,dp),helper(n-2,dp))
#     print(ans)
# cost = [1,100,1,1,1,100,1,1,100,1]
# minCostClimbingStairs2(cost)

#BOTTOM UP->O(n),O(n)
# def minCostClimbingStairs3(cost):
#     n = len(cost)
#     dp = [None]*(n+1)
#     dp[0] =  cost[0]
#     dp[1] =  cost[1]
#     for i in range(2,n):
#         dp[i] = cost[i] + min(dp[i-1],dp[i-2])
#     print(min(dp[n-1],dp[n-2]))

# cost = [10,15,20]
# minCostClimbingStairs3(cost)


#OPTIMIZED ->O(n),O(1)
def minCostClimbingStairs4(cost):
    n = len(cost)
    prev2 =  cost[0]
    prev1 =  cost[1]
    for i in range(2,n):
        current  = cost[i] + min(prev1,prev2)
        prev2 = prev1
        prev1 = current
    print(min(prev1,prev2))

cost = [10,15,20]
minCostClimbingStairs4(cost)


