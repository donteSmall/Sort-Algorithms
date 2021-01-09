def bubblesort(unsortedList):
    indexlength = len(unsortedList) - 1
    breakSort = False
   
   #Used when num of iteration is unknown
    while not breakSort:
        breakSort = True
        for idx in range(0,indexlength):
            if unsortedList[idx] > unsortedList[idx+1]:
                breakSort = False
                unsortedList[idx],unsortedList[idx+1] = unsortedList[idx+1], unsortedList[idx]

    return unsortedList

print(bubblesort([4,6,8,3,2,5,7,9]))

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
