# multiple query range
def prefix(arr,query)->list:
    n = len(arr)
    for i in range(1,n):
        arr[i]+=arr[i-1]
    return (list(arr[r]-arr[l-1] for l,r in query))
print(prefix([1,2,3,4,5],[(1,3),(2,4)]))