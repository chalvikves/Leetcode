class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = []
        false = []
        if not (len(s) % 2) == 0:
            return False
        for i in s:
            if i == '(' or i == '[' or i == '{':
                opened.append(i)

            if not opened:
                return False
            
            if i == ')':
                temp = opened.pop()
                if not temp == '(':
                    opened.append(temp)
                    false.append(i)
            elif i == ']': 
                temp = opened.pop()
                if not temp == '[':
                    opened.append(temp)
                    false.append(i)
            elif i == '}':
                temp = opened.pop()
                if not temp == '{':
                    opened.append(temp)
                    false.append(i)
            
        return len(opened) == 0 and len(false) == 0
    
    def runCases(self):
        print('Running case {[]}', self.isValid('{[]}'))
        print('Running case ()[]{}', self.isValid('()[]{}'))
        print('Running case (]', self.isValid('(]'))
        print('Running case ]', self.isValid(']'))
        print('Running case ){', self.isValid('){'))
        print('Running case (){}}{', self.isValid('(){}}{'))
        print('Running case ()', self.isValid('()'))
        print('Running case (])', self.isValid('(])'))
        print('Running case ([}}])', self.isValid('([}}])'))
        
    def lastTry(self):
        for i in s:
            if len(s) < 2:
                return False
            if s[0] == ')' or s[0] == ']' or s[0] == '}':
                if not opened:
                    return False
            if i == '(' or i == '[' or i == '{':
                opened.append(i)
            else:
                if not opened:
                    return False
                elif opened[len(opened)-1] == '(' and i == ')' :
                    opened.pop()
                elif opened[len(opened)-1] == '[' and i == ']':
                    opened.pop()
                elif opened[len(opened)-1] == '{' and i == '}':
                    opened.pop() 

def main():
    Solution().runCases()

if __name__ == '__main__':
    main()
    
