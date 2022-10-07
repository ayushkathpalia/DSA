#find min for start index to end and swap , increment index
nums= [10,40,29,90,60]

# for i in range(len(nums)):
#     min_i= i
#     for j in range(i+1,len(nums)):
#         if nums[j] < nums[min_i]:
#             min_i = j
#     nums[i],nums[min_i] = nums[min_i],nums[i]
# print(nums)    

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] < nums[i]:
            nums[i],nums[j]=nums[j],nums[i]

print(nums)



# Time -> O(n*n)
#Space -> O(1)

#Use when array is small


#A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in 
# sorted output as they appear in the input unsorted array

#Some examples of stable algorithms are Merge Sort, Insertion Sort, Bubble Sort, and Binary Tree Sort. 
# While, QuickSort, Heap Sort, and Selection sort are unstable sorting algorithms.

#An in-place algorithm is an algorithm that does not need an extra space and produces an output in the 
# same memory that contains the data by transforming the input ‘in-place’. However, a small constant extra
#  space used for variables is allowed.