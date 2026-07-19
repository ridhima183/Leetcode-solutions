import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        sum_odd = 0 
        sum_even = 0 

        for i in range(2*n + 1):
            if i%2==0:
                sum_even+=i
            else:
                sum_odd+=i

        gcd_pairs = math.gcd(sum_odd, sum_even)

        return gcd_pairs

        

        