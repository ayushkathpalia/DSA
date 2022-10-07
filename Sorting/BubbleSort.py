#Every round a largest element is reached at its position.
#Rounds = no of elements - 1

nums= [10,40,29,90,60]

for i in range(1,len(nums)):
    for j in range(len(nums)-i):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]

print(nums)





#OPTIMIZATION:
# if in any round , nums are not swapped then it is sorted.

#BEST CASE -> TIME ->O(n)
for i in range(1,len(nums)):
    swap = False
    for j in range(len(nums)-i):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            swap = True
    if not swap:
        break
print(nums)

#NOTE:

# if i =1
# then j range -> len(nums)-1

# if i = 0
# then j range -> len(nums)-i-j


#TIME -> O(n*n)
#SPACE -> O(1)