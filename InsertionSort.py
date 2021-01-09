'''

Best Case Complexity : O(n) Sorted array
Worst/Average Case Complexity : O(n^2) Unsorted array

Explaination : 
 During each iteration, the first remaining element of the 
 input is only compared with the right-most element of the 
 sorted subsection of the array

'''

def insertionSort(arr):
    idxLength = range(1, len(arr))
    for idx in idxLength:
        val_To_Sort = arr[idx]

        while arr[idx-1] > val_To_Sort and idx >0 :
            #swap index
            arr[idx], arr[idx-1] =  arr[idx-1], arr[idx]
            #increment down list to continue comparsion
            idx = idx -1 
    return arr

unsortedList= [4,6,8,3,2,5,7,9]
print(insertionSort(unsortedList))