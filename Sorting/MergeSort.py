def MergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        left_arr = arr[:mid]
        right_arr = arr[mid:]
        MergeSort(left_arr)
        MergeSort(right_arr)

        i,j = 0,0
        main_index =0


        #Sorting both arrays 
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[main_index] = left_arr[i]
                i+=1
            else:
                arr[main_index] = right_arr[j]
                j+=1
            main_index+=1

        #any arrays left 
        while i < len(left_arr):
            arr[main_index] = left_arr[i]
            i += 1
            main_index += 1
    
        while j < len(right_arr):
            arr[main_index] = right_arr[j]
            j += 1
            main_index += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    MergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)