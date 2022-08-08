'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''


class Palindrome:

    def isPalindrome(self, x):

        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        reversed_number = 0

        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x = x // 10

        return True if (x == reversed_number or x == reversed_number // 10) else False


class Solution:
    x = 121
    palindrome_obj = Palindrome()
    print(palindrome_obj.isPalindrome(x))
