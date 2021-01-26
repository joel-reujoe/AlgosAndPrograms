## Find max and min element in Array with min comparison


def getMinMax(A):
    
    max = 0
    min = 0
    if len(A)==1:        #if there is  only one element in the Array
        return A[0], A[0]

    if A[0] > A[1]:
        max = A[0]
        min = A[1]
    else:
        max = A[1]
        min = A[0]

    for i in range(2, len(A)):
        if A[i] < min:
            min = A[i]
        elif A[i] > max:
            max = A[i]

    return (min, max)
 
arr = [1000, 11, 445, 1, 330, 3000]
min,max = getMinMax(arr)
print("Minimum element is", min)
print("Maximum element is", max)


