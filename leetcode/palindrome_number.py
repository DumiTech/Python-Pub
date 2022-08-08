'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
'''


class Palindrome:

    def isPalindrome(self, x):

        # Declaring a temporary variable to keep x unmodified
        temp = x
        reversed_number = 0

        while (temp > 0):
            # Extracting last digit from temp
            last_digit = temp % 10
            # Moving last digit to it's correct base position in reversed_number
            reversed_number = reversed_number * 10 + last_digit
            # Removing last digit from temp
            temp = temp // 10

        return x == reversed_number


class Solution:
    x = 121
    palindrome_obj = Palindrome()
    print(palindrome_obj.isPalindrome(x))
