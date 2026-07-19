class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        digits = "123456789"
        result = []

        min_len = len(str(low))
        max_len = len(str(high))

        for length in range(min_len, max_len + 1):

            starts = 10 - length

            for i in range(starts):

                num = int(digits[i:i + length])

                if low <= num <= high:
                    result.append(num)

        return result
        '''result = []

        def number_check(num):
            digits = [] 

            while (num>0):
                digits.append(num%10)
                num = num//10

            digits.reverse()

            for i in range(len(digits)-1):
                if digits[i+1] != digits[i] + 1:
                    return False 

            return True 

        for i in range(low,high,1):
            if number_check(i):
                result.append(i)


        return result '''

