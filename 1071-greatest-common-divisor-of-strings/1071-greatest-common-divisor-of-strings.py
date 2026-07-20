import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_strings = math.gcd(len(str1), len(str2))
        candidate_string = str2[:gcd_strings]

        repeatstr1 = len(str1)//len(candidate_string)
        repeatstr2 = len(str2)//len(candidate_string)
        if candidate_string * repeatstr1 == str1 and candidate_string * repeatstr2 == str2:
            return candidate_string
        else:
            return ""


       

        