
def shipWithinDays(weights, days):
    def isPossible(mid):
        dayCount = 1
        weightSum = 0

        for i in range(len(weights)-1):
            if weightSum + weights[i] <= mid:
                weightSum+=weights[i]
            else:
                dayCount+=1
                if dayCount > days or weights[i] > mid:
                    return False
                weightSum+=weights[i]
        return True

    s = 0
    e = sum(weights)
    ans = -1
    mid = 0

    while s<=e:
        mid = int(s+(e-s)/2)
        if isPossible(mid):
            ans = mid
            e = mid-1
        else:
            s = mid+1
    return ans

arr = [3,2,2,4,1,4]
days = 3
res = shipWithinDays(arr,days)
print(res)
