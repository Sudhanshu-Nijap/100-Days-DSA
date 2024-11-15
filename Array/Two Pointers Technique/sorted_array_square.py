class Solution:
    def sortedSquares(self, arr):
        l = 0
        r = len(arr)-1
        while l<=r:
            if abs(arr[l]) > abs(arr[r]):
                arr[l]=arr[l]**2
                l+=1
            else:
                arr[r] = arr[r]**2
                r-=1
        arr.sort()
        return arr
