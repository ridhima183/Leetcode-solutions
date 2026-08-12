class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        
        string=str(x)
        return string==string[::-1]