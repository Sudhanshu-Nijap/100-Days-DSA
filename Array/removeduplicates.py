# Length of array -> n = len(arr)
# Initialize j = 1
# Loop -> for i in range(1,n)          (start from index 1 to length)
#             if arr[i] != arr[i-1]    
#             arr[j] = arr[i]          (store the element at index i in arr[j])
#             j+=1                     (increment j by 1)


class Solution:
    def dup(self,arr):
        n = len(arr)
        j = 1
        for i in range(1,n):
            if arr[i] != arr[i-1]:
                arr[j] = arr[i]
                j+=1
        
        
        return arr[:j]  

s = Solution()
print(s.dup([1,1,2,2,3,4,4,5]))

