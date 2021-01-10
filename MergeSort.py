'''
Two Sorted Arrays
[13,21,42,54]   [3,12,34,44]

          [3,12,13,21,34,42,44,54]
Naive Implemenation Steps : 
1) Start with comparing the first element in each of the arrays
2) Place smaller element into sorted array, the increment pointer to next index
3) Pointer of Larger element remains at its index until larger value is encounter


'''

def mergeSort(arr):
    if len(arr) <= 1:
        return 
        
    mid = len(arr)//2

    right = arr[:mid]
    left = arr[mid:]

    #recursive call on left & right parts of array
    # By default, mergeSort returns a sorted array
    mergeSort(left)
    mergeSort(right)
    
    merge_two_sorted_lists(left,right,arr)
    


def merge_two_sorted_lists(arr_A,arr_B,arr):
    len_A = len(arr_A)
    len_B = len(arr_B)

    idx = jdx = kdx = 0

    while idx < len_A and jdx < len_B:
        if arr_A[idx] <= arr_B[jdx]:
            arr[kdx] = arr_A[idx]
            idx +=  1
        else: 
            arr[kdx] = arr_B[jdx]
            jdx +=  1
        kdx +=1 
 
    '''
    Check for remaining values, 
    if so, add remaining values to sorted array 
    '''
    while idx < len_A:
        arr[kdx] = arr_A[idx]
        idx +=1
        kdx +=1 

    while jdx < len_B:
        arr[kdx] = arr_B[jdx]
        jdx +=1
        kdx +=1 

   



if __name__ == '__main__':
    
    # arr_A = [5,8,12,56]
    # arr_B = [7,9,45,51]
    # #Test Case for uneven length of arrays

    # arr_Aa = [5,8,12,56, 89, 100]
    # arr_Bb = [7,9,45,51]

    # print(merge_two_sorted_lists(arr_Aa,arr_Bb))

    unsorted_arr = [10,3,15,7,8,23,98,29]
    mergeSort(unsorted_arr)
    print(unsorted_arr)

    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        mergeSort(arr)
        print(arr)

   

