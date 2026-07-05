class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        banned = set(word.lower() for word in banned)
        words = []
        word = ""
        for ch in paragraph:
            if 'a' <= ch <= 'z':
                word += ch
            else:
                if word:
                    words.append(word)
                    word = ""
        if word:
            words.append(word)
        hashmap = {}
        for word in words:
            if word not in banned:
                if word in hashmap:
                    hashmap[word] += 1
                else:
                    hashmap[word] = 1
        maxFreq = 0
        ans = ""
        for key in hashmap:
            if hashmap[key] > maxFreq:
                maxFreq = hashmap[key]
                ans = key
        return ans