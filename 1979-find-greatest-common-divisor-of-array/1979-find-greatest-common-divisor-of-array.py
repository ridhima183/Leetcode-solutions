import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:

        max_array = max(nums)
        min_array = min(nums)

        gcd_array = math.gcd(max_array, min_array)

        return gcd_array


        