# A code that is using recursion but doesn't have good complexity.
# O(2^n) time complexity...
# Fibonacci 1:
def fibonacci_1(n):
    if n==2 or n==1:
        return 1
    else:
        res = fibonacci_1(n-1) + fibonacci_1(n-2)
        return res

# A code that has O(n) time complexity...
# Fibonacci 2:
res = [-1]* 1000 
def fibonacci_2(n):

    if n==2 or n==1:
        return 1
    else:
        if res[n]==-1:
            res[n] = (fibonacci_2(n-1) + fibonacci_2(n-2))
        return res[n]

# A python implementation of fibonacci number generator using Golden Ratio.
# This is only efficient for smaller value of 'n'.
# Time Complexity O(1)

from math import sqrt, floor

def fibonacci_3(n):
    phi = (1 + sqrt(5)) / 2
    return floor((phi**n - (1-phi)**n) / sqrt(5))

for i in range(1,10):
    print(f'First Method Output: {fibonacci_1(i)}')

for i in range(1,10):
    print(f'Second Method Output: {fibonacci_2(i)}')

for i in range(1,10):
    print(f'Third Method Output: {fibonacci_3(i)}')
