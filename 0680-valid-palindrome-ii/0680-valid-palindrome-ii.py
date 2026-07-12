class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrom(left,right): #this function checks for the basic palindrome
            while (left < right):
                if s[left] != s[right]:
                    return False 

                left +=1 
                right-=1
            return True 

        i = 0 
        j = len(s)-1

        while (i<j):
            if s[i] == s[j]:
                i+=1
                j-=1
            else : 
               return  isPalindrom(i+1,j) or isPalindrom(i,j-1)

        return True 

