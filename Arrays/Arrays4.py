def sort012(arr,n):
    lo = 0
    mid = 0
    high = n-1
    
    while mid<=high:
        if arr[mid]==0:
            arr[lo],arr[mid] = arr[mid], arr[lo]
            lo+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1

    return arr


a = [0,1,2,0,1,2]
n = len(a)
print(sort012(a,n))