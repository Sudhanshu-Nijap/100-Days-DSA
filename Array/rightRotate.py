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
#Length of arr -> n = len(arr)
# Make a temporary array to store the result -> temp = [0]*n
# Loop -> for i in range(n):
#            index = (i+k)%n        (Formula to right rotate)
#            temp[index] = arr[i]   (Store the elements in temp)


def rightrotation(arr,k):
    n = len(arr)
    temp =[0]*n
    for i in range(n):
        index = (i+k)%n
        temp[index] = arr[i]
    return temp
arr = [1,2,3,4,5,6,7]
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

#pattern4
def rotate(nums, k):
    n = len(nums)
    k = k%n
    nums.reverse()
    nums[:k]=reversed(nums[:k])
    nums[k:]=reversed(nums[k:])
    return nums
print(rotate([1,2,3,4,5],3))