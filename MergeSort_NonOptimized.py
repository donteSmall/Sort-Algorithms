'''
Two Sorted Arrays
[13,21,42,54]   [3,12,34,44]

          []
Naive Implemenation Steps : 
1) Start with comparing the first element in each of the arrays
2) Place smaller element into sorted array, the increment pointer to next index
3) Pointer of Larger element remains at its index until larger value is encounter


'''

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    right = arr[:mid]
    left = arr[mid:]
    #recursive call on left & right parts of array
    # By default, mergeSort returns a sorted array
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge_two_sorted_lists(left,right)
    


def merge_two_sorted_lists(arr_A,arr_B):
    sorted_list = []

    len_A = len(arr_A)
    len_B = len(arr_B)
    
    idx = jdx = 0

    while idx < len_A and jdx < len_B:
        
        if arr_A[idx] <= arr_B[jdx]:
            sorted_list.append(arr_A[idx])
            idx +=  1
        else: 
            sorted_list.append(arr_B[jdx])
            jdx +=  1
  
    while idx < len_A:
            sorted_list.append(arr_A[idx])
            idx +=1
    while jdx < len_B:
            sorted_list.append(arr_B[jdx])
            jdx +=1

    return sorted_list





if __name__ == '__main__':
    
    # arr_A = [5,8,12,56]
    # arr_B = [7,9,45,51]
    # #Test Case for uneven length of arrays
    # arr_Aa = [5,8,12,56, 89, 100]
    # arr_Bb = [7,9,45,51]
    # print(merge_two_sorted_lists(arr_Aa,arr_Bb))

    unsorted_arr = [10,3,15,7,8,23,98,29]
    print(mergeSort(unsorted_arr))

