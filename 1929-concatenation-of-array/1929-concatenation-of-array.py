class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans=[]*2*len(nums)
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        return ans
