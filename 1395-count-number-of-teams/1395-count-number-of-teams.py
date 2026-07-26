class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        ans = 0

        for j in range(n):
            left_smaller = left_greater = 0
            right_smaller = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_greater += 1
                else:
                    right_smaller += 1

            ans += left_smaller * right_greater
            ans += left_greater * right_smaller

        return ans