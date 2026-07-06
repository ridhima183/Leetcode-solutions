class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s=sorted(s)
        t=sorted(t)

        i=0
        j=0

        while (i<len(s) and j<len(t)):
            if s[i] != t[j] : 
                return t[j]
            i+=1
            j+=1

        return t[j]

