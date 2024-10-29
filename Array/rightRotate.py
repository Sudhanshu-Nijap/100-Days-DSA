# Brute force approach
# Pattern 
# 1. loop by k
# 2. last = arr[-1]
# 3. loop by (n-1,0,-1)
# 4. shift to right
# 5. arr[0] = last

def rightrotation(arr,k):
    n = len(arr)
    for _ in range(k):
        last = arr[-1]
        for i in range(n-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = last
    return arr
arr = [1,2,3,4,5]
print(rightrotation(arr,3)) 


# Better approach 1
# Pattern
# 1. temp array [0]*size of array
# 2. loop by n (size)
# 3. formula index = (i+k)%n
# 4. temp[index] =  arr[i]

def rightrotation(arr,k):
    n = len(arr)
    temp =[0]*n
    for i in range(n):
        index = (i+k)%n
        temp[index] = arr[i]
    return temp
arr = [1,2,3,4,5]
print(rightrotation(arr,3)) 

# Better approach 2
# Pattern
# reverse the array
# split by size (k) in  2 parts and reverse it
# split1 = arr[:k][::-1] ,  split2 = arr[k:][::-1]

def rightrotation(arr,k):
    new_arr = arr[::-1]
    split1 = new_arr[:k][::-1]
    split2 = new_arr[k:][::-1]
    return split1+split2
arr = [1,2,3,4,5]
print(rightrotation(arr,3)) 
