class Solution:
    def closetozero(self,arr):
        close = arr[0]

        for i in arr:
            if abs(i)  < abs(close):
                close = i
        
        if close<0 and abs(close) in arr:
            return  abs(close)
        else:
            return close
    
arr = [-4,-2,1,4,8]
s = Solution()
print(s.closetozero(arr))

