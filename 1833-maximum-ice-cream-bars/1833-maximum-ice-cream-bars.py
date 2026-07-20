class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        #build the frequency array 
        frequency_array = [0] * (max(costs)+1)
        for i in range(len(costs)):
            frequency_array[costs[i]]+=1

        count = 0 
        for i in range(1,len(frequency_array)):
            if coins < i:
                break
            frequency = frequency_array[i]
            affordable = coins//i #i==price 
            minimum = min(frequency, affordable)
            count += minimum  
            coins -= minimum * i 

        return count 



