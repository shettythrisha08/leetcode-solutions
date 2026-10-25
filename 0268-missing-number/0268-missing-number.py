class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        totalsum=(len(nums)*(len(nums)+1)) // 2
        total=sum(nums)

        return totalsum-total