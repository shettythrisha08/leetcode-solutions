class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums=sorted(nums)
        n=len(nums)
        return nums[n//2]