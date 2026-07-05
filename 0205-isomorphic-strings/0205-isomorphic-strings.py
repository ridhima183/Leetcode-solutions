class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m1={}
        m2={}

        for i in range(len(s)):
            c1=s[i]
            c2=t[i]

            if c1 not in m1 and c2 not in m2:
                m1[c1]=c2
                m2[c2]=c1

            elif c1 in m1 and c2 in m2:
                if m1[c1]!=c2 or m2[c2]!=c1:
                    return False 

            else:
                return False 

        return True 