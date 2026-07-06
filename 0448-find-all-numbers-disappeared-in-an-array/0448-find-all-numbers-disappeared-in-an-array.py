class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=[0]*len(nums)

        for i in range(len(nums)):
            count[nums[i]-1]+=1

        
        result=[]

        for i in range(len(count)):
            if count[i]==0:
                result.append(i+1)

        return result 

    