
def quick_sort(sequence):
    
    if len(sequence) <= 1:
        return sequence
    else:
        #removes and returns last element
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


listOfItems= [5,6,7,8,9,8,7,6,5,6,7,8, 9, 0]
print(quick_sort(listOfItems))

'''
Step by Step iteration of swap of index values:

if item < pivot:

    1: 0 9 8 8 2 7 Pop for Pivot(5)  Pivot Point --> 5
     
        0                      5
        ____________           __        __________
        Less than pivot        Pivot    More than pivot

     2: 9 8 8 2 7  Pivot Point --> 5
        
        0                      5         9
        ____________           __        __________
        Less than pivot        Pivot    More than pivot

     3: 8 8 2 7  Pivot Point --> 5
     
        0                      5          9 8
        ____________           __        __________
        Less than pivot        Pivot    More than pivot

     4: 8 2 7  Pivot Point --> 5
     
        0                      5          9 8 8
        ____________           __        __________
        Less than pivot        Pivot    More than pivot

      5: 2 7  Pivot Point --> 5
        
        0 2                     5          9 8 8
        ____________           __        __________
        Less than pivot        Pivot    More than pivot

      6: 2 7   Pivot Point --> 5
     
        0 2                     5          9 8 8 7
        ____________           __        __________
        Less than pivot        Pivot    More than pivot

       7: Empty List Pivot Point --> 5
     
     0 2                     5          9 8 8 7
     ____________           __        __________
    Less than pivot        Pivot    More than pivot

    Now recursively apply the same method to New list 

     0 2 5 9 8 8 pop(7)  Pivot Point --> 7

return list
'''

def concatlist(a,b,c):
    return a+b+c

print(concatlist([2,3],[7],[9,8]))