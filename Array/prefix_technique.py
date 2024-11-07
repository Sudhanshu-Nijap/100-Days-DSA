def prefix(arr,s,e):
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    sum = arr[e]-arr[s-1]
    return sum
arr=[1,2,3,4,5,6,7]
print(prefix(arr,2,4))

def prefix_sum(arr,s,e):
    sum = 0
    for i in range(s,e+1):
        sum = sum + arr[i]
    return sum
print(prefix_sum([1,2,3,4,5,6,7],0,6))
