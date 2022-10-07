def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = int(low + (high-low)/2)
        if arr[mid] < target:
            low = mid+1
        elif arr[mid] > target:
            high = mid+1
        else:
            return mid
    return -1

arr = [1,2,3,4,5]
target = 5
ans = binary_search(arr,target)
print(ans)