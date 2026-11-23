# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        arr=[]
        temp=head
        while temp is not None:
            arr.append(temp.val)
            temp=temp.next
        result=0
        for bit in arr:
            result=result*2+bit
        return result
