class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        temp=x
        while x !=0:
            num=x%10
            rev=rev*10+num
            x=x//10
        if rev==temp:
            return True
        return False
        
