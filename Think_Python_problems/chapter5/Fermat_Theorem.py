"""
Fermat’s Last Theorem says that there are no integers a, b, and c such that
a^n + b^n = c^n
for any values of n greater than 2.
"""

def prompt(a,b,c, n):
    prompt.a = int(input('Type a value for a: '))
    prompt.b = int(input('Type a value for b: '))
    prompt.c = int(input('Type a value for c: '))
    prompt.n = int(input('Type a value for n: '))
    print()

prompt(a='', b='', c='', n='')


def check_fermat(a,b,c,n):

    if n > 30:
        return

    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")
    check_fermat(a,b,c,n+1)

check_fermat(prompt.a, prompt.b, prompt.c, n=prompt.n)
