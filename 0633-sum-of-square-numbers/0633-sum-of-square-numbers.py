import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        left = 0 
        right = int(math.sqrt(c))

        Totalsum = 0

        while (left<=right):
            Totalsum = left*left + right*right
            
            if (Totalsum == c):
                return True 

            elif (Totalsum < c):
                left += 1

            else:
                right -= 1 

        return False

        