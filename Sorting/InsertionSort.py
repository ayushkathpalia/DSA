
nums= [10,40,29,90,60]

for i in range(1,len(nums)):
    key = nums[i]
    j=i-1
    while j>=0 and key < nums[j]:
        nums[j+1] = nums[j]
        j-=1
    nums[j+1] = key

print(nums)


#Time -> O(n*n)
#Space -> O(1)