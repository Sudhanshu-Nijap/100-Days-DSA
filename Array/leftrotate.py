def leftrotation(arr,k):
    n = len(arr)
    temp = [0]*n
    for i in range(n):
        index = (i-k)%n
        temp[index] = arr[i]
    return  temp


arr = [1,2,3,4,5]
print(leftrotation(arr,2)) 
