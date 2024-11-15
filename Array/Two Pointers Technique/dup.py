def count_duplicate(arr):
    l = 0
    r = len(arr)-1
    while l<=r:
        if arr[l] == arr[r]:
            return True
        l+=1
        r-+1
    return False
print(count_duplicate([1,2,3,4,3]))