class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = []

        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return "".join(reversed(ans))