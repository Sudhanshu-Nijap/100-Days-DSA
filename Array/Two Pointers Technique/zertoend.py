class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[r],nums[l] = nums[l],nums[r]
                l+=1
s = Solution()
print(s.moveZeros([1,8,0,5,0]))
