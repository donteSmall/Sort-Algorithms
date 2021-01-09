


def selectionSort(unsortedlist):


    for idx in range(0,len(unsortedlist)-1):
        minVal = idx

        for smallerVal_idx in range(idx + 1 ,len(unsortedlist)):
            if unsortedlist[smallerVal_idx] < unsortedlist[minVal]:
                minVal= smallerVal_idx 
            
            if minVal != idx:
                unsortedlist[minVal], unsortedlist[idx] = unsortedlist[idx], unsortedlist[minVal]

    return unsortedlist



print(selectionSort([7,8,9,7,5,6,7,8,9,0]))

'''
1: min(4) 4 6 2 8 7 
            ^
------------------
2: min(2) 4 6 2 8 7 
              ^ 
------------------
3: min(4) 4 6 2 8 7 
                ^ 
------------------
4: min(4) 4 6 2 8 7 
                  ^ 
End of iteration, swap min value idx
        *2nd iteration* 
1: Sortedlist[2] | 6 4 8 7 
                   ^ 
2: Sortedlist[2, 4, 6 ] |  8 7 
                           ^ 
2: Sortedlist[2, 4,6,7 ] | 8 
                         
'''