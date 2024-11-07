# Brute 
def twosum(arr,target):
    n = len(arr)
    for i in range(n-1):
        for j in range(1,n):
            if arr[i] + arr[j] == target:
                return i,j
print(twosum([2,7,11,15],9))

#Better
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

#two pointer technique
def twosum(arr,target):
    l = 0
    r = len(arr)-1
    while l<r:
        total = arr[l]+arr[r]
        if  total == target:
            return [l+1,r+1]
        elif total < target:
            l+=1
        else:
            r-=1

print(twosum([2,7,11,15],18))
