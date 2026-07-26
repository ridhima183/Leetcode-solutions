class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, float('-inf'), float('-inf')]

        for num in nums:
            temp = dp[:]

            for s in temp:
                if s != float('-inf'):
                    new_sum = s + num
                    dp[new_sum % 3] = max(dp[new_sum % 3], new_sum)

        return dp[0]