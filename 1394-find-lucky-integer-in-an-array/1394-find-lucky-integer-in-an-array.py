class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {} 
        for item in arr : 
            if item in count: 
                count[item]+=1

            else:
                count[item]=1

        max_LuckyNum = 0 

        for key,value in count.items():
            if key == value and key > max_LuckyNum :
                max_LuckyNum = key 

        return max_LuckyNum if max_LuckyNum else -1
