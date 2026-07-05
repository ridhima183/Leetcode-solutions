class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        start = 0          # Starting index of longest palindrome
        max_len = 1        # Length of longest palindrome

        # Function to expand around the center
        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # Adjust because loop stops after one extra expansion
            return left + 1, right - 1

        # Consider every character as a center
        for i in range(len(s)):

            # Odd length palindrome
            left1, right1 = expand(i, i)

            if right1 - left1 + 1 > max_len:
                start = left1
                max_len = right1 - left1 + 1

            # Even length palindrome
            left2, right2 = expand(i, i + 1)

            if right2 - left2 + 1 > max_len:
                start = left2
                max_len = right2 - left2 + 1

        return s[start:start + max_len]