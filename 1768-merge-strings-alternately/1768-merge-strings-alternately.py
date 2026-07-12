class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)

        result = []

        i = 0 
        j = 0 

        while (i<n and j<m):
            result.append(word1[i])
            i+=1
            result.append(word2[j])
            j+=1
        
        while (i<n):
            result.append(word1[i])
            i+=1

        while (j<m):
            result.append(word2[j])
            j+=1

        return "".join(result)




