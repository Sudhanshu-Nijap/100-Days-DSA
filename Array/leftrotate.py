# Better approach 1
# Pattern
# 1. temp array [0]*size of array
# 2. loop by n (size)
# 3. formula index = (i-k)%n
# 4. temp[index] =  arr[i]

def leftrotation(arr,k):
    n = len(arr)
    temp = [0]*n
    for i in range(n):
        index = (i-k)%n
        temp[index] = arr[i]
    return  temp


arr = [1,2,3,4,5]
print(leftrotation(arr,2)) 
