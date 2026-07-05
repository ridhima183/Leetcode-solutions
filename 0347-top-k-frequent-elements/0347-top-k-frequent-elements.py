class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        freq={}
        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1

        bucket=[[] for _ in range(n+1)]

        for key,value in freq.items():
            bucket[value].append(key)

        result=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result 
                    break