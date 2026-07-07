class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        freqs={}
        freqt={}

        for item in s:
            if item in freqs:
                freqs[item] +=1
            else:
                 freqs[item]=1

        for item in t:
            if item in freqt:
                freqt[item]+=1
            else:
                freqt[item]=1

        missing = 0

        for ch in freqs:
            if ch in freqt:
                if  freqs[ch] > freqt[ch]:
                    missing += (freqs[ch]-freqt[ch])
            else:
                missing+=freqs[ch] 

        return missing

