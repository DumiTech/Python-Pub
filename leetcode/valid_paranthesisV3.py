'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s:str) -> bool:
        while (('()' in s) or ('[]' in s) or ('{}' in s)):
            if '()' in s:
                s = s.replace('()', '')
            elif '[]' in s:
                s = s.replace('[]', '')
            elif '{}' in s:
                s = s.replace('{}', '')
        return s == ''


s = '()[]{}'
s1 = '{[()]}'
s2 = '[}'
obj = Solution()
print(obj.isValid(s))
print(obj.isValid(s1))
print(obj.isValid(s2))