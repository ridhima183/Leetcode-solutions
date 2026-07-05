class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        freq={}
        for item in nums:
            if item%2==0:
                if item in freq:
                    freq[item]+=1
                else:
                    freq[item]=1

        max_value=0
        min_key=-1
        for key,value in freq.items():
            if value>max_value:
                max_value=value
                min_key=key
            elif value==max_value and key<min_key: 
                min_key=key
        return min_key    
            
