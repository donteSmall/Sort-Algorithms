def bubblesort(arr):
    indexlength = len(arr) - 1
    breakSort = False
   
   #Used when num of iteration is unknown
    while not breakSort:
        breakSort = True
        for idx in range(0,indexlength):
            if arr[idx] > arr[idx+1]:
                breakSort = False
                arr[idx],arr[idx+1] = arr[idx+1], arr[idx]

    return arr

print(bubblesort([4,6,8,3,2,5,7,9]))

'''
Explain why the second paramater is 
need in for recursive version
'''
def bubbleSortRecursive(arr, lengthOfList): 
 
        # Base case
        if lengthOfList == 1:
            return "Length of list equals 1: " +str(arr)
 
        # One pass of bubble sort. After
        # this pass, the largest element
        # is moved (or bubbled) to end.
        for i in range(len(unsortedList) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i +1] = arr[i + 1],arr[i]
 
        # Largest element is fixed,
        #  recur for remaining array
        return bubbleSortRecursive(arr, lengthOfList - 1)

unsortedList= [4,6,8,3,2,5,7,9]

print(bubbleSortRecursive(unsortedList,len(unsortedList)))

'''
Step by Step iteration:

if idx < idx + 1:

    1: 8 3 5 10 7

    2: 3 8 5 10 7

    3: 3 5 8 10 7

    4: 3 5 8 7 10

    5: 3 5 7 8 10

return list
'''
