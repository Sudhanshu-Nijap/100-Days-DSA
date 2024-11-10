def twosum(arr,target):
    n = len(arr)
    h = {}
    for i in range(n):
        h[arr[i]] = i
    
    for i in range(n):
        y = target - arr[i]
        if y in h and h[y] != i:
            return [i,h[y]]
print(twosum([2,7,11,15],9))
