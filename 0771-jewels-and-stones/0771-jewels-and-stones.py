class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        find = {}

        for stone in stones : 
            if stone in find :
                find[stone] += 1
            else:
                find[stone] = 1 

        for jewel in jewels: 
            if jewel in find: 
                count += find[jewel]

        return count 
        