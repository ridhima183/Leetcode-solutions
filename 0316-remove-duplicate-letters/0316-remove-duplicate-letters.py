class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        for item in s :
            if item in count:
                count[item]+=1
            else:
                count[item]=1

        stack = []
        visited = set()   # Keeps track of characters already in the stack

        for ch in s:
            # Current character is no longer in the remaining string
            count[ch] -= 1

            # Skip if already present in the stack
            if ch in visited:
                continue

            # Remove larger characters if they appear again later
            while stack and ch < stack[-1] and count[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)