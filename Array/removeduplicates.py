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
print(s.dup([1,2,2,3,4,4,5]))

