"""
 If you are given three sticks, you may or may not be able to arrange them in a triangle.
For example, if one of the sticks is 12 inches long and the other two are one inch long, it is clear
that you will not be able to get the short sticks to meet in the middle. For any three lengths, there is
a simple test to see if it is possible to form a triangle:
“If any of the three lengths is greater than the sum of the other two, then you cannot
form a triangle. Otherwise, you can.”
"""

def is_triangle(a,b,c):
    if a + b < c or a + c < b or b + c < a:
        print('No')
    else:
        print('Yes')


def prompts(a,b,c):
    prompts.a = int(input('Enter the length of the first stick: '))
    prompts.b = int(input('Enter the length of the second stick: '))
    prompts.c = int(input('Enter the length of the third stick: '))

prompts(a='', b='', c='')

is_triangle(prompts.a, prompts.b, prompts.c)