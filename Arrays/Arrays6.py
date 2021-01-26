def Union(arr1, arr2, m, n):
    if m > n: # swap array with greater size
        tempp = arr1
        arr1 = arr2
        arr2 = tempp


        temp = m
        m = n
        n = temp

    arr1.sort()
    for i in range(0, m):
        print(arr1[i], end=" ") #print sorted first array

    for i in range(0, n):
        if (binarySearch(arr1, 0, m - 1, arr2[i]) == -1): #check if element in second array is not present in first array
            print(arr2[i], end=" ") #print if not present


def Intersection(arr1, arr2, m, n):
    if m > n: # swap array with greater size
        tempp = arr1
        arr1 = arr2
        arr2 = tempp


        temp = m
        m = n
        n = temp

    arr1.sort()
    for i in range(0, n):
        if (binarySearch(arr1, 0, m - 1, arr2[i]) != -1): #check if element in second array is present in first array
            print(arr2[i], end=" ") #print if present

    

def binarySearch(arr, l, r, x):
    if r>=l:
        mid = int(l+(r-1)/2)

        if arr[mid]== x: #check if middle element is the one
            return mid

        if arr[mid] > x: #check if the element is less than middle element
            return binarySearch(arr, l , mid-1, x)
        
        return binarySearch(arr, mid+1, r, x) # check if element is greater than middle element

    return -1


arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
m = len(arr1)
n = len(arr2)
 
# Function call
print("Union of two arrays is ")
Union(arr1, arr2, m, n)
print("\nIntersection of two arrays is ")
Intersection(arr1, arr2, m, n)