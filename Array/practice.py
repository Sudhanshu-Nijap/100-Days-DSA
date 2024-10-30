def duplicate(arr):
    n = len(arr)
    j = 1
    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j+=1
    return arr[:j]
print(duplicate([1,1,2,2,3,4]))

    