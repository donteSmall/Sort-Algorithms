def binary_search(arr, item):
    begin_idx = 0 
    end_idx = len(arr) - 1

    while begin_idx <= end_idx:
        midpoint = begin_idx + (end_idx - begin_idx) // 2
        midpoint_val = arr[midpoint]

        if midpoint_val == item:
            return midpoint
        elif item < midpoint_val:
            end_idx = midpoint - 1
        else: 
            begin_idx = midpoint + 1
    return None

sortedList = [4,5,6,7,8,10,11,12,13,14]
target_val = 6

print(binary_search(sortedList, target_val))

'''
Algorithm Complexity with SORTED LIST

Search is size of N element -->                  n = len(arr)
                                                 k = # steps --> k = log 2 n
                                                                    
  Each iteration, we reduce the sort by HALF
       n x 1     1     1     1     n
Start      -  X  _  X  _  X  _  =  _
           2     2     2     2     2^k 

'''