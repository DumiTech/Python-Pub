'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        s_len = len(s)
        for i in range(s_len):
            stack_len = len(stack)
            if stack_len == 0:
                stack.append(s[i])
            elif s[i] == ')' and stack[stack_len-1] == '(':
                stack.pop(stack_len-1)
            elif s[i] == ']' and stack[stack_len-1] == '[':
                stack.pop(stack_len-1)
            elif s[i] == '}' and stack[stack_len-1] == '{':
                stack.pop(stack_len-1)
            else:
                stack.append(s[i])
        return len(stack) == 0


s = '()[]{}'
s1 = '{[()]}'
s2 = '[}'
obj = Solution()
print(obj.isValid(s))
print(obj.isValid(s1))
print(obj.isValid(s2))