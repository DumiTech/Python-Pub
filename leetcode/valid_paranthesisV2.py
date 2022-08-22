'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s:str) -> bool:
        pair, stack = dict(('()', '[]', '{}')), []
        for x in s:
            if x in '([{':
                stack.append(x)
            elif (len(stack) == 0 or x != pair[stack.pop()]):
                return False
        return len(stack) == 0
        

s, s1, s2 = '()[]{}', '{[()]}', '[}'
obj = Solution()
print(obj.isValid(s), obj.isValid(s1), obj.isValid(s2))