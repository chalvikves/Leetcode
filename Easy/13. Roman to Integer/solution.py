class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        numerals = {
            'I' : 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = []
        length = len(s)
        
        for i, st in enumerate(s):
            if i+1 != length:
                if numerals[st] < numerals[s[i+1]]:
                    result.append(numerals[s[i+1]] - numerals[st])
                else:
                    result.append(numerals[st])
        
        return sum(result)