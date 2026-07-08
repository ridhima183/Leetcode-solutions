class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_val = ""

        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                if num[i] * 3 > max_val:
                    max_val = num[i] * 3 
        return max_val

