def allocateBooks(arr, n, m):
    def isPossible(mid):
        studentCount = 1
        pageSum = 0
        
        for i in range(n):
            if pageSum + arr[i] <= mid:
                pageSum+=arr[i]
            else:
                studentCount+=1
                if studentCount > m or arr[i] > mid:
                    return False
                pageSum=arr[i]
        return True

    s = 0
    e = sum(arr)
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

arr = [10,20,30,40]
m = 2
n = 4
res = allocateBooks(arr,n,m)
print(res)
