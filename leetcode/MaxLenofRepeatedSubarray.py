def findLength(nums1, nums2):
        dp = [[0] * (len(nums1)+1) for i in range(len(nums2)+1)]
        ans = 0
        for i in range(1, len(dp)): # for nums2
            for j in range(1, len(dp[0])): # for nums1
                if(nums2[i-1] == nums1[j-1]):
                    print(nums2[i-1],nums1[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1
                    print(dp)
                    ans = max(ans, dp[i][j])
        print(ans)

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

findLength(nums1,nums2)