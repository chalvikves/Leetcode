class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sb = s[::-1]
        count = 0
        for c in sb:
            if c == ' ' and count == 0:
                continue
            elif c == ' ':
                break
            count += 1

        return count