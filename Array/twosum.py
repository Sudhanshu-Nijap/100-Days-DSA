# Brute 
def twosum(arr,target):
    n = len(arr)
    for i in range(n-1):
        for j in range(1,n):
            if arr[i] + arr[j] == target:
                return i,j
print(twosum([2,7,11,15],9))