# Assign first element of the array in variable close -> close = arr[0]
# Loop each element in the array -> for i in arr:
# Check condition -> if abs(i) < abs(close):
#                       close = abs(i)
# Check if the closest element is -ve as well as +ve ->
# if close < 0 and abs(close) in arr:
#   return abs(close)     
# else:
#   return close 

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

