class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        max_len = 0 

        for num in numSet:
            if num - 1 in numSet:
                continue
            else:
                if num - 1 not in numSet:
                    current = num 
                    length = 1
                    while ( current + 1 ) in numSet: 
                        current +=1 
                        length += 1 
                    max_len = max(length, max_len)
        return max_len
