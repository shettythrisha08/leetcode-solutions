class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum=0
        for cust in accounts:
            total=0
            for money in cust:
                total+=money
            maximum=max(maximum,total)
        return maximum