class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result=[[1]]
        for i in range(numRows-1):
            new_row=[]
            new_row.append(1)
            prev=result[-1]
            for j in range(len(prev)-1):
                new_row.append(prev[j]+prev[j+1])
            new_row.append(1)
            result.append(new_row)
        return result