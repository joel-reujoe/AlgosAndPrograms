#find the kth smallest element

def kthSmallest(arr, k):
    arr = sorted(arr) #sort in ascending order
    return arr[k-1] #return k-1th element which is th correct value


arr = [1000, 11, 445, 1, 330, 3000]
print(kthSmallest(arr=arr, k=3))
