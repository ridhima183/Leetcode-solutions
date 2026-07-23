class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        leftMax = [0] * n
        rightMax = [0] * n

        # Prefix maximum
        leftMax[0] = nums[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i])

        # Suffix maximum
        rightMax[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i])

        ans = 0

        # Try every possible middle index j
        for j in range(1, n - 1):
            value = (leftMax[j - 1] - nums[j]) * rightMax[j + 1]
            ans = max(ans, value)

        return ans
        