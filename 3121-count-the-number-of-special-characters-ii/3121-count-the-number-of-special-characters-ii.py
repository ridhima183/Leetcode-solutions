class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower_index = {}
        first_upper_index = {}

        for i in range(len(word)):
            ch = word[i]

            if ch.islower(): #every time the lower character is encountered, keep updating the index until the last one is found.
                last_lower_index[ch] = i
            else: 
                if ch not in first_upper_index: # checking if the character already exists then skip because the first index is required 
                    first_upper_index[ch] = i 

        count = 0 
        for ch in last_lower_index: 
            if ch.upper() in first_upper_index: 
                if last_lower_index[ch] < first_upper_index[ch.upper()]:
                    count += 1 


        return count







                
        