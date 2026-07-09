class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        hash_set=set()
        for i in range(n):
            if nums[i]>0:
                hash_set.add(nums[i])
        if not hash_set :
            return 1

        for i in range(1,len(nums)+1):
            if i not in hash_set:
                return i 
        return (max(nums)+1)


        