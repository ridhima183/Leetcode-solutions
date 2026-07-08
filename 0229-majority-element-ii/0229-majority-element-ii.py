class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {} 
        for item in nums :
            if item in count :
                count[item] +=1
            else:
                count[item] = 1 

        result = [] 

        for key in count: 
            if count[key] > len(nums) // 3 :
                result.append(key)

        return result 