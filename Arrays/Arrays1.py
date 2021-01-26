##Reverse an Array

def reverseList(A, start, end): ##Iterative
    while start < end:
        A[start], A[end] = A[end],A[start]
        start+=1
        end-=1


def reverseListRecursive(A, start, end): ##Recursive
    if start>=end:
        return
    A[start], A[end] = A[end],A[start]
    reverseListRecursive(A,start+1,end-1)


A = [1, 2, 3, 4, 5, 6]
print(A)
reverseListRecursive(A, 0, 5)
print("Reversed list is")
print(A)
