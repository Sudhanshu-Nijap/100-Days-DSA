def remove(arr,val):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] != val:
            arr[count] = arr[i]
            count+=1
    return count
print(remove([0,1,2,2,3,0,4,2],2))  # Output: [